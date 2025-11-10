<style>
body {
  background-color: #f5f0e8;
  color: #2c2416;
  font-family: 'Courier New', Courier, monospace;
  max-width: 900px;
  margin: 0 auto;
  padding: 20px;
}

h1, h2, h3 {
  font-family: 'Courier New', Courier, monospace;
  color: #2c2416;
  font-weight: bold;
}

.tabs {
  display: flex;
  gap: 0;
  margin-bottom: 40px;
  border: 3px solid #2c2416;
  background: #2c2416;
}

.tab-button {
  flex: 1;
  padding: 14px 20px;
  border: none;
  background: #d4c4a8;
  cursor: pointer;
  font-size: 15px;
  font-weight: bold;
  font-family: 'Courier New', Courier, monospace;
  color: #2c2416;
  transition: all 0.2s;
  border-right: 3px solid #2c2416;
}

.tab-button:last-child {
  border-right: none;
}

.tab-button:hover {
  background: #bfa882;
  transform: translateY(-2px);
}

.tab-button.active {
  background: #8b7355;
  color: #f5f0e8;
}

.tab-content {
  display: none;
}

.tab-content.active {
  display: block;
  animation: fadeIn 0.3s;
}

@keyframes fadeIn {
  from { opacity: 0; transform: translateY(10px); }
  to { opacity: 1; transform: translateY(0); }
}

.topic-list {
  list-style: none;
  padding: 0;
  margin: 0;
}

.topic-list li {
  margin: 20px 0;
  padding: 18px;
  border: 3px solid #2c2416;
  background: #fff;
  box-shadow: 6px 6px 0 #2c2416;
  transition: all 0.2s;
}

.topic-list li:hover {
  transform: translate(-2px, -2px);
  box-shadow: 8px 8px 0 #2c2416;
}

.topic-list li a {
  color: #8b4513;
  font-weight: bold;
  font-size: 17px;
  text-decoration: none;
  font-family: 'Courier New', Courier, monospace;
}

.topic-list li a:hover {
  text-decoration: underline;
}

.topic-list li .topic-desc {
  color: #5c4a3a;
  font-size: 13px;
  margin-top: 8px;
  font-family: 'Courier New', Courier, monospace;
}

.intro-text {
  color: #5c4a3a;
  margin-bottom: 30px;
  line-height: 1.8;
  padding: 15px;
  background: #fff;
  border: 2px solid #2c2416;
  border-left: 8px solid #8b7355;
}
</style>

<div class="tabs">
  <button class="tab-button active" onclick="openTab(event, 'grammatik')">📖 Grammatik</button>
  <button class="tab-button" onclick="openTab(event, 'vokabular')">📚 Vokabular</button>
  <button class="tab-button" onclick="openTab(event, 'info')">ℹ️ Info</button>
</div>

<div id="grammatik" class="tab-content active">

## Grammatik

<p class="intro-text">
Auf dieser Seite findest du systematische Erklärungen deutscher Grammatikregeln mit Beispielen und Übungen für das C1-Niveau. Jedes Thema enthält ausführliche Erklärungen und praktische Übungen.
</p>

### Verfügbare Themen:

<ul class="topic-list">
  <li>
    <a href="grammatik/01_vergangenheitsformen/erklaerung.md">01. Vergangenheitsformen (Perfekt & Plusquamperfekt)</a>
    <div class="topic-desc">Bildung und Verwendung von Perfekt und Plusquamperfekt • Niveau: B2-C1</div>
  </li>
</ul>

</div>

<div id="vokabular" class="tab-content">

## Vokabular

<p class="intro-text">
Hier findest du thematisch organisierte Vokabellisten mit deutschen Wörtern und englischen Übersetzungen. Alle Übersetzungen wurden mit professionellen Tools erstellt und sind nach Themen sortiert.
</p>

### Verfügbare Themen:

<ul class="topic-list">
  <li>
    <a href="vokabular/01_essen/">01. Essen und Küche</a>
    <div class="topic-desc">Besteck, Küchengeräte, Mahlzeiten, Gewürze und Koch-Verben • 50+ Vokabeln</div>
  </li>
</ul>

</div>

<div id="info" class="tab-content">

## Info

<p class="intro-text">
Diese Lernplattform ist mein persönliches Tool zur Vorbereitung auf das C1-Zertifikat in Deutsch. Alle Inhalte werden kontinuierlich erweitert und verbessert.
</p>

### Lernmethode

1. **Grammatik verstehen** - Regeln lernen und internalisieren
2. **Vokabular aufbauen** - Thematische Wortschatzarbeit
3. **Üben, üben, üben** - Regelmäßige Übungen und Anwendung

### Struktur

- **Grammatik**: Systematische Erklärungen deutscher Grammatikregeln mit Beispielen und Übungen
- **Vokabular**: Thematisch organisierte Vokabellisten mit deutschen Wörtern und englischen Übersetzungen

---

*Letzte Aktualisierung: November 2025*

</div>

<script>
function openTab(evt, tabName) {
  // Hide all tab contents
  var tabContents = document.getElementsByClassName("tab-content");
  for (var i = 0; i < tabContents.length; i++) {
    tabContents[i].classList.remove("active");
  }

  // Remove active class from all buttons
  var tabButtons = document.getElementsByClassName("tab-button");
  for (var i = 0; i < tabButtons.length; i++) {
    tabButtons[i].classList.remove("active");
  }

  // Show the selected tab and mark button as active
  document.getElementById(tabName).classList.add("active");
  evt.currentTarget.classList.add("active");
}
</script>
