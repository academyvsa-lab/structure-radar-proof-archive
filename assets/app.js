function fmtPct(x) {
  if (x === null || x === undefined) return "-";
  return (x * 100).toFixed(1) + "%";
}
function fmtHours(seconds) {
  if (seconds === null || seconds === undefined) return "-";
  const h = seconds / 3600;
  if (h < 1) return Math.round(seconds / 60) + "m";
  if (h < 48) return h.toFixed(1) + "h";
  return (h / 24).toFixed(1) + "d";
}
function card(label, value, hint) {
  return `
    <div class="card">
      <div class="label">${label}</div>
      <div class="value">${value}</div>
      <div class="hint">${hint}</div>
    </div>
  `;
}
async function loadManifest() {
  const res = await fetch("manifest.json", { cache: "no-store" });
  if (!res.ok) throw new Error("Failed to load manifest.json");
  return await res.json();
}
function renderKPIs(manifest) {
  const latest = manifest.weeks[0];
  const total = latest?.totals?.alerts ?? "-";
  const win = latest?.resolved?.win_rate ?? null;
  const open = latest?.totals?.open ?? "-";
  const kpi = document.getElementById("kpiCards");
  kpi.innerHTML = [
    card("Latest week", latest.week, "UTC weekly window"),
    card("Total alerts", total, "All emitted alerts"),
    card("Resolved win rate", fmtPct(win), "Targets vs stops only"),
    card("Open pipeline", open, "Alerts still OPEN")
  ].join("");
}
function renderTable(manifest) {
  const tbody = document.getElementById("weeksTbody");
  tbody.innerHTML = manifest.weeks.map(w => {
    const reportHref = `weekly/${w.week}/report.md`;
    const snapHref = `weekly/${w.week}/snapshot.json`;
    const medianRes = w.validation_v2?.median_resolution_seconds ?? null;
    const maxLoss = w.validation_v2?.max_consecutive_losses ?? null;
    return `
      <tr>
        <td><span class="tag">${w.week}</span></td>
        <td>${w.totals.alerts}</td>
        <td>${w.resolved.count}</td>
        <td>${fmtPct(w.resolved.win_rate)}</td>
        <td>${w.totals.expired}</td>
        <td>${w.totals.open}</td>
        <td>${fmtHours(medianRes)}</td>
        <td>${(maxLoss === null || maxLoss === undefined) ? "-" : maxLoss}</td>
        <td>
          <a href="${reportHref}">Report</a>
          <span class="muted"> | </span>
          <a href="${snapHref}">Snapshot</a>
        </td>
      </tr>
    `;
  }).join("");
  const updated = document.getElementById("lastUpdated");
  updated.textContent = "Last updated: " + (manifest.generated_at_utc || "unknown");
}
(async function main() {
  try {
    const manifest = await loadManifest();
    if (!manifest.weeks || manifest.weeks.length === 0) {
      document.getElementById("weeksTbody").innerHTML =
        `<tr><td colspan="9" class="muted">No weeks published yet.</td></tr>`;
      document.getElementById("kpiCards").innerHTML = "";
      return;
    }
    renderKPIs(manifest);
    renderTable(manifest);
  } catch (e) {
    const tbody = document.getElementById("weeksTbody");
    tbody.innerHTML = `<tr><td colspan="9" class="muted">${e.message}</td></tr>`;
  }
})();
