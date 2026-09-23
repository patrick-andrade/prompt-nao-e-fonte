(() => {
  "use strict";

  const data = JSON.parse(document.getElementById("fm-data").textContent);
  const DEBT = "GGXWDG_NGDP";
  const PRIMARY = "GGXONLB_NGDP";
  const featured = new Set(["BRA", "MEX", "CHL", "IND", "IDN"]);
  const number1 = new Intl.NumberFormat("pt-BR", { minimumFractionDigits: 1, maximumFractionDigits: 1 });
  const integer = new Intl.NumberFormat("pt-BR");
  const collator = new Intl.Collator("pt-BR", { sensitivity: "base", numeric: true });
  const byKey = new Map();
  const countryByIso = new Map();
  const years = Array.from({ length: 30 }, (_, i) => 2000 + i);

  for (const row of data.rows) {
    countryByIso.set(row.iso3, row.country);
    const key = `${row.iso3}|${row.year}`;
    if (!byKey.has(key)) byKey.set(key, { debt: null, primary: null });
    byKey.get(key)[row.indicator_code === DEBT ? "debt" : "primary"] = row.value;
  }

  const countries = [...countryByIso.keys()].sort((a, b) => collator.compare(countryByIso.get(a), countryByIso.get(b)));
  let year = 2025;
  let selectedIso = countryByIso.has("BRA") ? "BRA" : countries[0];
  let sortKey = "country";
  let sortDirection = 1;

  const el = (id) => document.getElementById(id);
  const current = (iso, requestedYear = year) => byKey.get(`${iso}|${requestedYear}`) || { debt: null, primary: null };
  const present = (value) => typeof value === "number" && Number.isFinite(value);
  const show = (value, signed = false) => present(value) ? `${signed && value > 0 ? "+" : ""}${number1.format(value)}` : "—";
  const raw = (value) => present(value) ? String(value).replace(".", ",") : "— (ausente)";
  const normalized = (value) => value.normalize("NFD").replace(/[\u0300-\u036f]/g, "").toLocaleLowerCase("pt-BR");

  function svgElement(tag, attrs = {}, content = "") {
    const element = document.createElementNS("http://www.w3.org/2000/svg", tag);
    for (const [name, value] of Object.entries(attrs)) element.setAttribute(name, String(value));
    if (content) element.textContent = content;
    return element;
  }

  function addLine(svg, x1, y1, x2, y2, className) {
    svg.appendChild(svgElement("line", { x1, y1, x2, y2, class: className }));
  }

  function addText(svg, x, y, label, attrs = {}) {
    svg.appendChild(svgElement("text", { x, y, ...attrs }, label));
  }

  function ticks(min, max, n = 4) {
    return Array.from({ length: n + 1 }, (_, i) => min + (max - min) * i / n);
  }

  function updateCountryOptions(query = "") {
    const select = el("country-select");
    select.replaceChildren();
    const search = normalized(query.trim());
    const matches = countries.filter((iso) => !search || normalized(`${countryByIso.get(iso)} ${iso}`).includes(search));
    if (search && !matches.includes(selectedIso)) {
      select.add(new Option(`${countryByIso.get(selectedIso)} (${selectedIso}) · foco atual`, selectedIso));
    }
    for (const iso of matches) select.add(new Option(`${countryByIso.get(iso)} (${iso})`, iso));
    select.value = selectedIso;
    if (matches.length === 0) select.setAttribute("aria-label", "Nenhuma economia corresponde ao filtro; foco atual preservado");
    else select.setAttribute("aria-label", "Selecionar economia");
  }

  function yearRecords() {
    return countries.map((iso) => ({ iso3: iso, country: countryByIso.get(iso), ...current(iso) }));
  }

  function renderCoverage(records) {
    const debt = records.filter((r) => present(r.debt)).length;
    const primary = records.filter((r) => present(r.primary)).length;
    const both = records.filter((r) => present(r.debt) && present(r.primary)).length;
    el("coverage-year").textContent = String(year);
    el("total-economies").textContent = integer.format(countries.length);
    el("count-both").textContent = integer.format(both);
    el("count-debt").textContent = integer.format(debt);
    el("count-primary").textContent = integer.format(primary);
    el("count-incomplete").textContent = integer.format(countries.length - both);
    el("scatter-note").textContent = `${integer.format(both)} economias com par completo; ${integer.format(countries.length - both)} sem par completo não entram na dispersão. O ponto selecionado só aparece quando ambos os valores existem.`;
  }

  function renderScatter(records) {
    const svg = el("scatter");
    svg.replaceChildren();
    const valid = records.filter((r) => present(r.debt) && present(r.primary));
    svg.setAttribute("aria-label", `Dispersão de dívida bruta e saldo primário em ${year}; ${valid.length} economias com ambos os indicadores`);
    if (!valid.length) {
      addText(svg, 480, 255, "Sem pares completos neste ano", { "text-anchor": "middle" });
      return;
    }

    const left = 84, right = 927, top = 28, bottom = 445;
    const debts = valid.map((r) => r.debt);
    const primaries = valid.map((r) => r.primary);
    const rawXMin = Math.min(0, ...debts), rawXMax = Math.max(1, ...debts);
    const xPad = (rawXMax - rawXMin) * .045;
    const xMin = rawXMin < 0 ? rawXMin - xPad : 0;
    const xMax = rawXMax + xPad;
    const rawYMin = Math.min(0, ...primaries), rawYMax = Math.max(0, ...primaries);
    const yPad = Math.max(1, (rawYMax - rawYMin) * .08);
    const yMin = rawYMin - yPad, yMax = rawYMax + yPad;
    const x = (value) => left + (value - xMin) / (xMax - xMin) * (right - left);
    const y = (value) => bottom - (value - yMin) / (yMax - yMin) * (bottom - top);

    for (const tick of ticks(xMin, xMax, 5)) {
      const sx = x(tick);
      addLine(svg, sx, top, sx, bottom, "grid");
      addText(svg, sx, bottom + 22, number1.format(tick), { "text-anchor": "middle" });
    }
    for (const tick of ticks(yMin, yMax, 4)) {
      const sy = y(tick);
      addLine(svg, left, sy, right, sy, "grid");
      addText(svg, left - 11, sy + 4, number1.format(tick), { "text-anchor": "end" });
    }
    if (yMin < 0 && yMax > 0) addLine(svg, left, y(0), right, y(0), "zero");
    addLine(svg, left, top, left, bottom, "axis");
    addLine(svg, left, bottom, right, bottom, "axis");
    addText(svg, (left + right) / 2, 503, "Dívida bruta do governo geral (% do PIB)", { "text-anchor": "middle" });
    addText(svg, 18, (top + bottom) / 2, "Saldo primário do governo geral (% do PIB)", { transform: `rotate(-90 18 ${(top + bottom) / 2})`, "text-anchor": "middle" });

    const ordered = valid.slice().sort((a, b) => {
      const priority = (r) => r.iso3 === selectedIso ? 2 : featured.has(r.iso3) ? 1 : 0;
      return priority(a) - priority(b);
    });
    for (const row of ordered) {
      const isSelected = row.iso3 === selectedIso;
      const isFeatured = featured.has(row.iso3);
      const dot = svgElement("circle", {
        cx: x(row.debt), cy: y(row.primary), r: isSelected ? 9 : isFeatured ? 6.5 : 4,
        fill: isSelected ? "#67d7c6" : isFeatured ? "#f1c978" : "#8ea9ba",
        stroke: isSelected ? "#ffffff" : "none", "stroke-width": isSelected ? 2 : 0,
        class: "dot", tabindex: 0, role: "button",
        "aria-label": `Selecionar ${row.country}. Dívida ${show(row.debt)} e saldo primário ${show(row.primary, true)} por cento do PIB em ${year}`
      });
      dot.appendChild(svgElement("title", {}, `${row.country} (${row.iso3}) · dívida ${show(row.debt)} · primário ${show(row.primary, true)} · ${year}`));
      dot.addEventListener("click", () => selectCountry(row.iso3));
      dot.addEventListener("keydown", (event) => {
        if (event.key === "Enter" || event.key === " ") { event.preventDefault(); selectCountry(row.iso3); }
      });
      svg.appendChild(dot);
    }
  }

  function renderFocus() {
    const record = current(selectedIso);
    const country = countryByIso.get(selectedIso);
    el("focus-year").textContent = String(year);
    el("focus-title").textContent = country;
    el("focus-iso").textContent = selectedIso;
    el("focus-debt").textContent = show(record.debt);
    el("focus-primary").textContent = show(record.primary, true);
    el("source-identification").textContent = `${country} (${selectedIso}) · ${year} · ${data.vintage} · ${data.source} · ${data.unit}.`;
    el("source-debt").textContent = raw(record.debt);
    el("source-primary").textContent = raw(record.primary);
    el("trend-subtitle").textContent = `${country} (${selectedIso}) · valores disponíveis da edição ${data.vintage}`;
    for (const button of el("featured-picks").querySelectorAll("button")) {
      button.setAttribute("aria-pressed", button.dataset.iso === selectedIso ? "true" : "false");
    }
  }

  function renderTrend(svgId, noteId, field, color, label) {
    const svg = el(svgId);
    svg.replaceChildren();
    const values = years.map((yearValue) => ({ year: yearValue, value: current(selectedIso, yearValue)[field] }));
    const valid = values.filter((item) => present(item.value));
    const country = countryByIso.get(selectedIso);
    svg.setAttribute("aria-label", `${label} de ${country}, 2000 a 2029; ${valid.length} anos com valor`);
    el(noteId).textContent = `${valid.length} de 30 anos com valor. Lacunas não são conectadas.`;
    if (!valid.length) { addText(svg, 360, 165, "Sem valores disponíveis", { "text-anchor": "middle" }); return; }

    const left = 68, right = 688, top = 20, bottom = 268;
    const vals = valid.map((r) => r.value);
    const rawMin = Math.min(0, ...vals), rawMax = Math.max(0, ...vals);
    const pad = Math.max(1, (rawMax - rawMin) * .1);
    const yMin = field === "debt" && rawMin >= 0 ? 0 : rawMin - pad;
    const yMax = rawMax + pad;
    const x = (y) => left + (y - 2000) / 29 * (right - left);
    const y = (v) => bottom - (v - yMin) / (yMax - yMin) * (bottom - top);

    for (const tick of ticks(yMin, yMax, 4)) {
      const sy = y(tick);
      addLine(svg, left, sy, right, sy, "grid");
      addText(svg, left - 9, sy + 4, number1.format(tick), { "text-anchor": "end" });
    }
    for (const tick of [2000, 2005, 2010, 2015, 2020, 2025, 2029]) {
      const sx = x(tick);
      addLine(svg, sx, top, sx, bottom, "grid");
      addText(svg, sx, bottom + 21, String(tick), { "text-anchor": "middle" });
    }
    if (yMin < 0 && yMax > 0) addLine(svg, left, y(0), right, y(0), "zero");
    addLine(svg, x(year), top, x(year), bottom, "zero");
    addLine(svg, left, top, left, bottom, "axis");
    addLine(svg, left, bottom, right, bottom, "axis");
    addText(svg, (left + right) / 2, 317, "Ano", { "text-anchor": "middle" });
    addText(svg, 16, (top + bottom) / 2, "% do PIB", { transform: `rotate(-90 16 ${(top + bottom) / 2})`, "text-anchor": "middle" });

    let segment = [];
    const flush = () => {
      if (segment.length > 1) svg.appendChild(svgElement("path", { d: segment.join(" "), fill: "none", stroke: color, "stroke-width": 3, "stroke-linejoin": "round" }));
      segment = [];
    };
    for (const item of values) {
      if (!present(item.value)) { flush(); continue; }
      segment.push(`${segment.length === 0 ? "M" : "L"}${x(item.year).toFixed(2)},${y(item.value).toFixed(2)}`);
    }
    flush();
    for (const item of valid) {
      const dot = svgElement("circle", { cx: x(item.year), cy: y(item.value), r: item.year === year ? 5.7 : 2.7, fill: color, stroke: item.year === year ? "#fff" : "none", "stroke-width": 1.8 });
      dot.appendChild(svgElement("title", {}, `${country} · ${item.year} · ${label}: ${show(item.value)} % do PIB`));
      svg.appendChild(dot);
    }
  }

  function renderTable(records) {
    const query = normalized(el("table-search").value.trim());
    const filtered = records.filter((r) => !query || normalized(`${r.country} ${r.iso3}`).includes(query));
    filtered.sort((a, b) => {
      if (sortKey === "debt" || sortKey === "primary") {
        if (!present(a[sortKey])) return present(b[sortKey]) ? 1 : collator.compare(a.country, b.country);
        if (!present(b[sortKey])) return -1;
        return sortDirection * (a[sortKey] - b[sortKey]) || collator.compare(a.country, b.country);
      }
      return sortDirection * collator.compare(a[sortKey], b[sortKey]) || collator.compare(a.country, b.country);
    });
    const body = el("table-body");
    const fragment = document.createDocumentFragment();
    for (const row of filtered) {
      const tr = document.createElement("tr");
      if (featured.has(row.iso3)) tr.classList.add("featured");
      if (row.iso3 === selectedIso) tr.classList.add("selected-row");
      const country = document.createElement("td"); country.textContent = row.country; tr.appendChild(country);
      const iso = document.createElement("td"); iso.textContent = row.iso3; tr.appendChild(iso);
      const debt = document.createElement("td"); debt.className = "numeric"; debt.textContent = show(row.debt); tr.appendChild(debt);
      const primary = document.createElement("td"); primary.className = "numeric"; primary.textContent = show(row.primary, true); tr.appendChild(primary);
      const actionCell = document.createElement("td");
      const action = document.createElement("button"); action.type = "button"; action.className = "table-action";
      action.textContent = row.iso3 === selectedIso ? "Em foco" : "Selecionar";
      action.setAttribute("aria-label", `Colocar ${row.country} em foco`);
      action.addEventListener("click", () => selectCountry(row.iso3));
      actionCell.appendChild(action); tr.appendChild(actionCell);
      fragment.appendChild(tr);
    }
    body.replaceChildren(fragment);
    el("table-year").textContent = String(year);
    el("table-count").textContent = `${integer.format(filtered.length)} de ${integer.format(countries.length)} economias`;
    for (const th of document.querySelectorAll("thead th")) th.removeAttribute("aria-sort");
    const active = document.querySelector(`thead button[data-sort="${sortKey}"]`);
    active.parentElement.setAttribute("aria-sort", sortDirection === 1 ? "ascending" : "descending");
  }

  function render() {
    const records = yearRecords();
    renderCoverage(records);
    renderScatter(records);
    renderFocus();
    renderTrend("debt-trend", "debt-note", "debt", "#67d7c6", "Dívida bruta");
    renderTrend("primary-trend", "primary-note", "primary", "#f1c978", "Saldo primário");
    renderTable(records);
  }

  function selectCountry(iso) {
    if (!countryByIso.has(iso)) return;
    selectedIso = iso;
    el("country-search").value = "";
    updateCountryOptions();
    render();
    el("country-select").focus();
  }

  for (const y of years) el("year-select").add(new Option(String(y), String(y)));
  el("year-select").value = String(year);
  for (const iso of ["BRA", "MEX", "CHL", "IND", "IDN"]) {
    if (!countryByIso.has(iso)) continue;
    const button = document.createElement("button");
    button.type = "button";
    button.dataset.iso = iso;
    button.textContent = `${countryByIso.get(iso)} · ${iso}`;
    button.addEventListener("click", () => selectCountry(iso));
    el("featured-picks").appendChild(button);
  }
  updateCountryOptions();
  el("meta-vintage").textContent = data.vintage;
  el("footer-source").textContent = data.source;
  el("year-select").addEventListener("change", (event) => { year = Number(event.target.value); render(); });
  el("country-search").addEventListener("input", (event) => updateCountryOptions(event.target.value));
  el("country-search").addEventListener("keydown", (event) => {
    if (event.key !== "Enter") return;
    const query = normalized(event.target.value.trim());
    const match = countries.find((iso) => normalized(`${countryByIso.get(iso)} ${iso}`).includes(query));
    if (match && query) { event.preventDefault(); selectCountry(match); }
  });
  el("country-select").addEventListener("change", (event) => selectCountry(event.target.value));
  el("table-search").addEventListener("input", () => renderTable(yearRecords()));
  for (const button of document.querySelectorAll("thead button[data-sort]")) {
    button.addEventListener("click", () => {
      const newKey = button.dataset.sort;
      if (newKey === sortKey) sortDirection *= -1;
      else { sortKey = newKey; sortDirection = newKey === "debt" || newKey === "primary" ? -1 : 1; }
      renderTable(yearRecords());
    });
  }
  render();
})();
