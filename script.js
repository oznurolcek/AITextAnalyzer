const API_URL = "http://127.0.0.1:8000";

const textArea = document.getElementById("textInput");
const counter = document.getElementById("counter");
const resultBox = document.getElementById("result");

textArea.addEventListener("input", () => {
  counter.innerText = `${textArea.value.length} karakter`;
});

textArea.addEventListener("keydown", e => {
  if ((e.metaKey || e.ctrlKey) && e.key === "Enter") {
    analyzeText();
  }
});

function showSkeleton() {
  resultBox.style.display = "block";
  document.getElementById("summaryText").innerHTML = `
    <div class="skeleton"></div>
    <div class="skeleton skeleton-block"></div>
    <div class="skeleton skeleton-block"></div>
  `;
  document.getElementById("keywords").innerHTML = `
    <div class="skeleton" style="width:80px"></div>
    <div class="skeleton" style="width:60px"></div>
  `;
}

async function analyzeText() {
  const button = document.getElementById("analyzeBtn");
  const sentimentBadge = document.getElementById("sentimentBadge");

  const text = textArea.value.trim();
  if (!text) return alert("Metin giriniz");

  button.disabled = true;
  showSkeleton();

  try {
    const res = await fetch(`${API_URL}/analyze`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ text })
    });

    const data = await res.json();

    document.getElementById("summaryText").innerText = data.summary;
    sentimentBadge.innerText = data.sentiment;
    sentimentBadge.className = `badge ${data.sentiment}`;

    const kw = document.getElementById("keywords");
    kw.innerHTML = "";
    data.keywords.forEach(k => {
      const span = document.createElement("span");
      span.className = "keyword";
      span.innerText = k;
      kw.appendChild(span);
    });

  } catch (e) {
    alert("Hata oluştu");
  } finally {
    button.disabled = false;
  }
}

function exportTXT() {
  const text = document.getElementById("summaryText").innerText;
  const blob = new Blob([text], { type: "text/plain" });
  const a = document.createElement("a");
  a.href = URL.createObjectURL(blob);
  a.download = "analysis.txt";
  a.click();
}

function exportPDF() {
  window.print();
}

function resetAll() {
  textArea.value = "";
  counter.innerText = "0 karakter";
  resultBox.style.display = "none";
}
