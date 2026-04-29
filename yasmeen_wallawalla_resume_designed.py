import { useState, useMemo } from "react";
import { BarChart, Bar, XAxis, YAxis, Tooltip, ResponsiveContainer, PieChart, Pie, Cell, CartesianGrid, Area, AreaChart, RadarChart, PolarGrid, PolarAngleAxis, PolarRadiusAxis, Radar } from "recharts";

const GROWTH_DATA = [
  { role: "AI/ML Engineer", growth: 40, category: "AI & ML", color: "#a855f7" },
  { role: "Data Scientist", growth: 34, category: "Data Science", color: "#00d2ff" },
  { role: "Prompt Engineer", growth: 33, category: "AI & ML", color: "#a855f7" },
  { role: "Cloud Security Engineer", growth: 31, category: "Cybersecurity", color: "#ff6b35" },
  { role: "Info Security Analyst", growth: 29, category: "Cybersecurity", color: "#ff6b35" },
  { role: "AI Research Scientist", growth: 28, category: "AI & ML", color: "#a855f7" },
  { role: "MLOps Engineer", growth: 27, category: "AI & ML", color: "#a855f7" },
  { role: "DevSecOps Engineer", growth: 26, category: "Cybersecurity", color: "#ff6b35" },
  { role: "Computer/Info Research Scientist", growth: 26, category: "Data Science", color: "#00d2ff" },
  { role: "Platform Engineer", growth: 25, category: "Cloud & Infra", color: "#7b68ee" },
  { role: "Site Reliability Engineer", growth: 24, category: "Cloud & Infra", color: "#7b68ee" },
  { role: "Kubernetes Engineer", growth: 23, category: "Cloud & Infra", color: "#7b68ee" },
  { role: "Penetration Tester", growth: 22, category: "Cybersecurity", color: "#ff6b35" },
  { role: "Actuary", growth: 22, category: "Data Science", color: "#00d2ff" },
  { role: "Quantitative Analyst", growth: 21, category: "Finance", color: "#32cd32" },
  { role: "Operations Research Analyst", growth: 21, category: "Data Science", color: "#00d2ff" },
  { role: "Data Engineer", growth: 20, category: "Data Science", color: "#00d2ff" },
  { role: "Cloud Architect", growth: 20, category: "Cloud & Infra", color: "#7b68ee" },
  { role: "FinTech Engineer", growth: 19, category: "Finance", color: "#32cd32" },
  { role: "Security Architect", growth: 18, category: "Cybersecurity", color: "#ff6b35" },
  { role: "Blockchain Developer", growth: 18, category: "Specialized", color: "#20b2aa" },
  { role: "Software Developer", growth: 17, category: "Software Eng", color: "#e94560" },
  { role: "Full-Stack Developer", growth: 17, category: "Software Eng", color: "#e94560" },
  { role: "DevOps Engineer", growth: 16, category: "Cloud & Infra", color: "#7b68ee" },
  { role: "UX Researcher", growth: 16, category: "Product", color: "#ff69b4" },
  { role: "Product Manager (Technical)", growth: 15, category: "Product", color: "#ff69b4" },
  { role: "Digital/AI Consultant", growth: 15, category: "Consulting", color: "#00bfff" },
  { role: "Robotics Engineer", growth: 14, category: "Specialized", color: "#20b2aa" },
  { role: "Financial Analyst", growth: 12, category: "Finance", color: "#32cd32" },
  { role: "Network Engineer", growth: 11, category: "Networking", color: "#ffd700" },
  { role: "Management Consultant", growth: 11, category: "Consulting", color: "#00bfff" },
  { role: "Database Administrator", growth: 9, category: "Cloud & Infra", color: "#7b68ee" },
  { role: "Systems Administrator", growth: 5, category: "IT Ops", color: "#50c878" },
  { role: "IT Support Specialist", growth: 4, category: "IT Ops", color: "#50c878" },
];

const DECADE_PROJECTIONS = {
  "AI & Machine Learning": { workers2026: 220, growthRate: 0.30, color: "#a855f7" },
  "Data Science & Analytics": { workers2026: 520, growthRate: 0.25, color: "#00d2ff" },
  "Cybersecurity": { workers2026: 1340, growthRate: 0.22, color: "#ff6b35" },
  "Cloud & Infrastructure": { workers2026: 850, growthRate: 0.18, color: "#7b68ee" },
  "Software Engineering": { workers2026: 2100, growthRate: 0.15, color: "#e94560" },
  "Finance (Tech-Adjacent)": { workers2026: 1800, growthRate: 0.10, color: "#32cd32" },
  "Consulting": { workers2026: 1050, growthRate: 0.09, color: "#00bfff" },
  "Product & Design": { workers2026: 480, growthRate: 0.13, color: "#ff69b4" },
  "Networking": { workers2026: 420, growthRate: 0.06, color: "#ffd700" },
  "IT Operations & Support": { workers2026: 950, growthRate: 0.04, color: "#50c878" },
  "Specialized Engineering": { workers2026: 340, growthRate: 0.14, color: "#20b2aa" },
};

const MARKET_SIZE = [
  { name: "Software Engineering", value: 2100, color: "#e94560" },
  { name: "Finance (Tech-Adjacent)", value: 1800, color: "#32cd32" },
  { name: "Cybersecurity", value: 1340, color: "#ff6b35" },
  { name: "Consulting", value: 1050, color: "#00bfff" },
  { name: "IT Operations & Support", value: 950, color: "#50c878" },
  { name: "Cloud & Infrastructure", value: 850, color: "#7b68ee" },
  { name: "Data Science & Analytics", value: 520, color: "#00d2ff" },
  { name: "Product & Design", value: 480, color: "#ff69b4" },
  { name: "Networking", value: 420, color: "#ffd700" },
  { name: "Specialized Engineering", value: 340, color: "#20b2aa" },
  { name: "AI & Machine Learning", value: 220, color: "#a855f7" },
];
const TOTAL_WORKERS = MARKET_SIZE.reduce((s, d) => s + d.value, 0);

const TECH_MARKET = [
  { name: "Software Engineering", value: 2100, color: "#e94560" },
  { name: "Cybersecurity", value: 1340, color: "#ff6b35" },
  { name: "IT Operations & Support", value: 950, color: "#50c878" },
  { name: "Cloud & Infrastructure", value: 850, color: "#7b68ee" },
  { name: "Data Science & Analytics", value: 520, color: "#00d2ff" },
  { name: "Product & Design", value: 480, color: "#ff69b4" },
  { name: "Networking", value: 420, color: "#ffd700" },
  { name: "Specialized Engineering", value: 340, color: "#20b2aa" },
  { name: "AI & Machine Learning", value: 220, color: "#a855f7" },
];
const TECH_TOTAL = TECH_MARKET.reduce((s, d) => s + d.value, 0);

const BIZ_MARKET = [
  { name: "Finance", value: 1800, color: "#32cd32" },
  { name: "Consulting", value: 1050, color: "#00bfff" },
];
const BIZ_TOTAL = BIZ_MARKET.reduce((s, d) => s + d.value, 0);

const renderColoredLabel = (props) => {
  const { cx, cy, midAngle, outerRadius, name, percent, fill } = props;
  const RADIAN = Math.PI / 180;
  const radius = outerRadius + 28;
  const x = cx + radius * Math.cos(-midAngle * RADIAN);
  const y = cy + radius * Math.sin(-midAngle * RADIAN);
  const anchor = x > cx ? "start" : "end";
  return (
    <text x={x} y={y} textAnchor={anchor} fill={fill} fontSize={10} fontWeight={500} fontFamily="'DM Sans', sans-serif">
      {name.replace(" & ", " & ").split(" ").slice(0, 2).join(" ")} {(percent * 100).toFixed(0)}%
    </text>
  );
};

// ═══ CAREER RANKING (all scores 1-5, higher = better for career seeker) ═══
const DIMS = [
  { key: "stability", label: "Job Stability", icon: "\u{1F6E1}" },
  { key: "salary", label: "Salary", icon: "\u{1F4B0}" },
  { key: "entryEase", label: "Entry Ease", icon: "\u{1F6AA}" },
  { key: "lowCompetition", label: "Low Competition", icon: "\u{1F3C1}" },
  { key: "growth", label: "Projected Growth", icon: "\u{1F4C8}" },
  { key: "entryOpportunity", label: "Entry Opportunity", icon: "\u{1F3AF}" },
  { key: "prepTime", label: "Low Prep Time", icon: "\u{23F1}" },
  { key: "levelUp", label: "Level-Up Ease", icon: "\u{1F680}" },
];

// prepTime scoring (higher = less time to acquire basic entry skills):
//   5.0 = <150 hours, 4.0 = 150-300 hrs, 3.0 = 300-600 hrs, 2.0 = 600-1200 hrs, 1.0 = 1200+ hrs
// levelUp scoring (higher = faster salary/role progression once in):
//   5.0 = 2x salary in <3 yrs + clear ladder, 1.0 = stagnant or gatekept progression

const RANKING_RAW = [
  { name: "Cybersecurity", color: "#ff6b35", stability: 4.8, salary: 4.0, entryEase: 4.0, lowCompetition: 4.5, growth: 4.7, entryOpportunity: 4.5, prepTime: 4.0, levelUp: 4.5,
    prepHours: "150\u2013300 hrs (Security+ cert)", levelUpNotes: "SOC T1 $65K \u2192 Security Engineer $150K in 3\u20135 yrs. Clear specialization ladder.",
    verdict: "Best overall bet", why: "Massive 4.8M global workforce gap means employers are desperate. SOC Analyst (Tier 1) is accessible with just a Security+ cert and no degree. Salaries grow fast once you're in. Threats only increase \u2014 this field can't be outsourced or fully automated.", entryPath: "Security+ cert \u2192 SOC Analyst T1 \u2192 specialize in cloud security or pen testing", timeToEntry: "3\u20136 months with cert prep" },
  { name: "Cloud & Infrastructure", color: "#7b68ee", stability: 4.5, salary: 4.3, entryEase: 3.5, lowCompetition: 3.5, growth: 4.2, entryOpportunity: 3.8, prepTime: 3.5, levelUp: 4.5,
    prepHours: "200\u2013400 hrs (AWS CCP + SAA)", levelUpNotes: "Cloud Engineer $110K \u2192 Cloud Architect $220K in 4\u20136 yrs. Each new cert = raise.",
    verdict: "High ceiling, clear cert path", why: "Every company runs on cloud \u2014 it's essential infrastructure. AWS/Azure/GCP certs provide a clear entry ladder. DevOps and SRE roles pay exceptionally well ($130K\u2013$210K). Platform engineering is the hot new specialty for 2026.", entryPath: "AWS Cloud Practitioner \u2192 Solutions Architect Associate \u2192 DevOps or SRE role", timeToEntry: "6\u201312 months" },
  { name: "Data Science & Analytics", color: "#00d2ff", stability: 4.0, salary: 4.0, entryEase: 3.2, lowCompetition: 2.8, growth: 4.5, entryOpportunity: 3.5, prepTime: 3.0, levelUp: 3.8,
    prepHours: "300\u2013600 hrs (SQL + Python + Tableau)", levelUpNotes: "Data Analyst $75K \u2192 Data Scientist $130K \u2192 Senior $180K. Ceiling without pivoting to ML.",
    verdict: "Strong growth, competitive entry", why: "BLS projects 34% growth for data scientists \u2014 4th fastest occupation overall. Data Analyst is the accessible entry point. The field rewards quantitative rigor, which means a math + CS background is a major advantage. Some junior analyst roles face AI automation pressure.", entryPath: "Data Analyst (SQL + Python + Tableau) \u2192 Data Scientist \u2192 Senior DS / ML Engineer", timeToEntry: "0\u20136 months with CS degree" },
  { name: "AI & Machine Learning", color: "#a855f7", stability: 4.2, salary: 4.8, entryEase: 1.8, lowCompetition: 1.5, growth: 5.0, entryOpportunity: 2.0, prepTime: 1.5, levelUp: 4.8,
    prepHours: "1500+ hrs (math, ML theory, coding, projects)", levelUpNotes: "AI Eng $140K \u2192 Senior $220K \u2192 Staff/Research $300K+. Fastest salary growth of any track.",
    verdict: "Highest ceiling, hardest entry", why: "Fastest-growing category with a 12% salary premium over general SWE. But entry typically requires MS/PhD or exceptional portfolio. AI Engineer (LLMs/RAG) is more accessible than ML Research. Competition is fierce \u2014 every CS grad wants in. Best approached via SWE first, then lateral move.", entryPath: "SWE role \u2192 build AI side projects \u2192 AI Engineer \u2192 ML Engineer \u2192 Research", timeToEntry: "1\u20133 years after BS (or direct with MS)" },
  { name: "Software Engineering", color: "#e94560", stability: 4.0, salary: 4.0, entryEase: 3.3, lowCompetition: 2.5, growth: 3.5, entryOpportunity: 3.0, prepTime: 2.0, levelUp: 4.3,
    prepHours: "1000\u20132000 hrs (DSA + languages + projects)", levelUpNotes: "Junior $90K \u2192 Senior $170K in 5 yrs \u2192 Staff $250K. FAANG adds 50\u2013100% via RSU.",
    verdict: "The universal foundation", why: "Largest category and the default for CS grads. BLS projects 17% growth. Entry-level is saturated (73% drop in junior hiring as AI automates routine tasks), but mid/senior demand remains very strong. Best used as a launchpad into higher-paying specializations like AI, cloud, or security.", entryPath: "Internships \u2192 Junior SWE \u2192 Mid SWE \u2192 specialize (cloud, AI, security)", timeToEntry: "0\u20136 months with CS degree + internships" },
  { name: "Product & Design", color: "#ff69b4", stability: 3.5, salary: 3.5, entryEase: 3.0, lowCompetition: 2.5, growth: 3.5, entryOpportunity: 3.0, prepTime: 3.0, levelUp: 3.5,
    prepHours: "400\u2013800 hrs (UX or PM portfolio + case prep)", levelUpNotes: "APM $130K \u2192 PM $170K \u2192 Senior PM $220K. Fast at FAANG, slower elsewhere.",
    verdict: "Creative + technical hybrid", why: "Technical PM is high-leverage but extremely competitive to break into. UX/UI has strong demand but lower salary ceiling than engineering. Portfolio and side projects matter more than credentials here. APM programs at Google/Meta are the golden ticket.", entryPath: "UX bootcamp or APM program \u2192 Associate PM \u2192 PM \u2192 Senior PM", timeToEntry: "6\u201318 months" },
  { name: "Specialized Engineering", color: "#20b2aa", stability: 4.0, salary: 4.0, entryEase: 2.0, lowCompetition: 3.5, growth: 3.5, entryOpportunity: 2.5, prepTime: 1.5, levelUp: 3.8,
    prepHours: "2000+ hrs (deep CS + domain expertise)", levelUpNotes: "Niche skills = slow early, but principal engineer comp ($300K+) comes faster once established.",
    verdict: "Niche expertise = job security", why: "Compiler engineers, distributed systems, robotics \u2014 these are hard to hire for because the skills are rare. Lower competition once in, but the entry bar is high (deep CS, often MS preferred). Great for people who love going deep on hard problems.", entryPath: "Strong CS fundamentals \u2192 systems-heavy SWE role \u2192 specialize over 2\u20133 years", timeToEntry: "2\u20134 years to full specialization" },
  { name: "Finance", color: "#32cd32", stability: 3.2, salary: 4.8, entryEase: 2.0, lowCompetition: 1.5, growth: 3.0, entryOpportunity: 2.0, prepTime: 2.2, levelUp: 4.5,
    prepHours: "800\u20131500 hrs (modeling, networking, CFA/FMVA)", levelUpNotes: "IB Analyst $100K \u2192 Associate $175K (3 yrs) \u2192 VP $300K \u2192 MD $500K\u2013$1M+.",
    verdict: "Highest pay, gatekept entry", why: "IB/PE/quant comp is unmatched ($200K\u2013$1M+), but entry is heavily gatekept by target schools, GPA, networking, and grueling interviews. Cyclical industry \u2014 layoffs hit hard in downturns. FinTech is the more accessible door that leverages CS + finance skills without the prestige filter.", entryPath: "Finance internships \u2192 IB Analyst or FinTech SWE \u2192 PE/VC/Quant (with MBA or MS)", timeToEntry: "Recruit 1\u20132 years before graduation" },
  { name: "Consulting", color: "#00bfff", stability: 3.0, salary: 4.0, entryEase: 2.2, lowCompetition: 1.8, growth: 3.0, entryOpportunity: 2.5, prepTime: 3.0, levelUp: 4.5,
    prepHours: "300\u2013600 hrs (case prep + behavioral + networking)", levelUpNotes: "Analyst $95K \u2192 Consultant $150K \u2192 Manager $200K \u2192 Partner $500K+. 2 yrs per level.",
    verdict: "Best exit options, up-or-out", why: "Consulting is a career accelerator \u2014 unmatched breadth of experience and exit options (PE, corp strategy, startups). But it's up-or-out, hours are intense, and recruiting is prestige-driven. Starting salaries flat in 2026. Tech consulting at Big 4 is more accessible than MBB strategy.", entryPath: "Case prep \u2192 MBB/Big 4 Analyst \u2192 2\u20133 yrs \u2192 exit or MBA \u2192 return as Associate", timeToEntry: "Recruit fall of junior year" },
  { name: "Networking", color: "#ffd700", stability: 3.5, salary: 3.0, entryEase: 4.0, lowCompetition: 4.0, growth: 2.5, entryOpportunity: 4.0, prepTime: 4.0, levelUp: 2.8,
    prepHours: "150\u2013300 hrs (CCNA cert)", levelUpNotes: "Network Engineer $85K \u2192 Senior $125K \u2192 Architect $160K. Slower than cloud or security.",
    verdict: "Stable, accessible, lower ceiling", why: "Clear cert path (CCNA \u2192 CCNP \u2192 CCIE) with low competition. Every org needs networks. Growth is slow as SDN and cloud networking reduce headcount. Best as a stepping stone to cloud or security roles where network knowledge is a differentiator.", entryPath: "CCNA cert \u2192 Network Tech \u2192 Network Engineer \u2192 Architect or pivot to cloud/security", timeToEntry: "3\u20136 months with cert" },
  { name: "IT Operations & Support", color: "#50c878", stability: 3.0, salary: 2.5, entryEase: 4.8, lowCompetition: 4.5, growth: 2.0, entryOpportunity: 4.8, prepTime: 4.8, levelUp: 2.0,
    prepHours: "100\u2013200 hrs (CompTIA A+)", levelUpNotes: "Help Desk $45K \u2192 SysAdmin $80K = 3\u20135 yrs. Ceiling low unless you pivot to cloud/security.",
    verdict: "Easiest entry, best stepping stone", why: "The most accessible category in tech \u2014 help desk jobs require no degree and minimal certs. Low salary ceiling ($40K\u2013$60K entry), but it's the fastest way into tech. Many cybersecurity and cloud pros started here. Think of it as a 1\u20132 year springboard, not a destination.", entryPath: "CompTIA A+ \u2192 Help Desk \u2192 SysAdmin \u2192 pivot to cloud, security, or DevOps", timeToEntry: "1\u20133 months" },
];

const WEIGHTS = { stability: 0.14, salary: 0.12, entryEase: 0.15, lowCompetition: 0.11, growth: 0.14, entryOpportunity: 0.10, prepTime: 0.12, levelUp: 0.12 };
const RANKING_SCORED = RANKING_RAW.map(d => {
  const composite = DIMS.reduce((s, dim) => s + d[dim.key] * WEIGHTS[dim.key], 0);
  return { ...d, composite: Math.round(composite * 100) / 100 };
}).sort((a, b) => b.composite - a.composite);

// ═══ COMPONENTS ═══

function ScoreBar({ value }) {
  const pct = (value / 5) * 100;
  const bg = pct >= 80 ? "#22c55e" : pct >= 60 ? "#eab308" : pct >= 40 ? "#f97316" : "#ef4444";
  return (
    <div style={{ display: "flex", alignItems: "center", gap: 6 }}>
      <div style={{ flex: 1, height: 5, background: "rgba(255,255,255,0.06)", borderRadius: 3 }}>
        <div style={{ height: "100%", borderRadius: 3, width: `${pct}%`, background: bg }} />
      </div>
      <span style={{ fontFamily: "'JetBrains Mono'", fontSize: 10, fontWeight: 600, color: bg, minWidth: 22, textAlign: "right" }}>{value.toFixed(1)}</span>
    </div>
  );
}

function GradeCircle({ score }) {
  const pct = (score / 5) * 100;
  const grade = pct >= 85 ? "A+" : pct >= 78 ? "A" : pct >= 72 ? "A-" : pct >= 66 ? "B+" : pct >= 60 ? "B" : pct >= 54 ? "B-" : pct >= 48 ? "C+" : "C";
  const gc = pct >= 78 ? "#22c55e" : pct >= 60 ? "#eab308" : "#f97316";
  return (
    <div style={{ textAlign: "center" }}>
      <div style={{ width: 42, height: 42, borderRadius: "50%", border: `3px solid ${gc}`, display: "flex", alignItems: "center", justifyContent: "center", fontFamily: "'JetBrains Mono'", fontSize: 14, fontWeight: 700, color: gc }}>{grade}</div>
      <div style={{ fontFamily: "'JetBrains Mono'", fontSize: 10, color: "#666", marginTop: 2 }}>{score.toFixed(2)}</div>
    </div>
  );
}

const CTooltipBar = ({ active, payload }) => {
  if (!active || !payload?.length) return null;
  const d = payload[0].payload;
  return (<div style={{ background: "#1a1a2e", border: "1px solid #333", borderRadius: 8, padding: "10px 14px", fontSize: 12, color: "#ddd" }}><div style={{ fontWeight: 600, color: "#fff" }}>{d.role}</div><div style={{ color: d.color }}>{d.category}</div><div style={{ marginTop: 4, fontFamily: "'JetBrains Mono'", fontWeight: 700, color: "#e94560" }}>+{d.growth}%</div></div>);
};
const CTooltipLine = ({ active, payload, label }) => {
  if (!active || !payload?.length) return null;
  return (<div style={{ background: "#1a1a2e", border: "1px solid #333", borderRadius: 8, padding: "10px 14px", fontSize: 12, color: "#ddd" }}><div style={{ fontWeight: 600, color: "#fff" }}>{label}</div>{payload.map((p, i) => (<div key={i} style={{ color: p.color, marginTop: 2 }}>{p.name}: <span style={{ fontFamily: "'JetBrains Mono'", fontWeight: 600 }}>{p.value?.toLocaleString()}K</span></div>))}</div>);
};
const CTooltipPie = ({ active, payload }) => {
  if (!active || !payload?.length) return null;
  const d = payload[0].payload;
  return (<div style={{ background: "#1a1a2e", border: "1px solid #333", borderRadius: 8, padding: "10px 14px", fontSize: 12, color: "#ddd" }}><div style={{ fontWeight: 600, color: "#fff" }}>{d.name}</div><div style={{ fontFamily: "'JetBrains Mono'" }}><span style={{ color: d.color, fontWeight: 700 }}>{d.value.toLocaleString()}K</span> workers</div><div style={{ color: "#888", marginTop: 2 }}>{((d.value / TOTAL_WORKERS) * 100).toFixed(1)}%</div></div>);
};

// ═══ MAIN ═══
const TABS = ["Fastest Growing", "Decade Projections", "Market Size", "Career Ranking"];

export default function Dashboard() {
  const [tab, setTab] = useState(3);
  const [selectedCats, setSelectedCats] = useState(["AI & Machine Learning", "Cybersecurity", "Software Engineering", "Data Science & Analytics", "Cloud & Infrastructure"]);
  const [expandedRank, setExpandedRank] = useState(0);
  const [radarPicks, setRadarPicks] = useState([0, 3]);

  const decadeCats = Object.keys(DECADE_PROJECTIONS);
  const mergedDecadeData = useMemo(() => {
    const years = [];
    for (let y = 2026; y <= 2036; y++) { const row = { year: y }; selectedCats.forEach(cat => { const d = DECADE_PROJECTIONS[cat]; if (d) row[cat] = Math.round(d.workers2026 * Math.pow(1 + d.growthRate / 10, y - 2026)); }); years.push(row); }
    return years;
  }, [selectedCats]);

  const radarData = useMemo(() => DIMS.map(dim => {
    const row = { subject: dim.label };
    radarPicks.forEach(idx => { const d = RANKING_SCORED[idx]; if (d) row[d.name] = d[dim.key]; });
    return row;
  }), [radarPicks]);

  const toggleRadar = (idx) => setRadarPicks(prev => prev.includes(idx) ? prev.filter(i => i !== idx) : prev.length >= 3 ? [...prev.slice(1), idx] : [...prev, idx]);

  return (
    <div style={{ fontFamily: "'DM Sans', 'Segoe UI', sans-serif", background: "#0a0a14", color: "#e0e0e8", minHeight: "100vh" }}>
      <style>{`
        @import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;500&display=swap');
        *{box-sizing:border-box;margin:0;padding:0}
        ::-webkit-scrollbar{width:5px}::-webkit-scrollbar-track{background:#0a0a14}::-webkit-scrollbar-thumb{background:#333;border-radius:3px}
        .tb{cursor:pointer;padding:7px 13px;border-radius:8px;border:1px solid rgba(255,255,255,0.08);font-size:11px;font-weight:600;transition:all .2s;font-family:inherit;background:rgba(255,255,255,0.03);color:#777}
        .tb:hover{border-color:rgba(255,255,255,0.2);color:#bbb}.tb.a{background:rgba(233,69,96,0.12);border-color:#e94560;color:#e94560}
        .cc{cursor:pointer;padding:4px 10px;border-radius:12px;font-size:10px;font-weight:500;transition:all .15s;font-family:inherit;border:1px solid}
        .rc{border-radius:12px;border:1px solid rgba(255,255,255,0.06);overflow:hidden;transition:all .2s;cursor:pointer}
        .rc:hover{border-color:rgba(255,255,255,0.12)}
      `}</style>

      <div style={{ padding: "24px 20px 14px" }}>
        <h1 style={{ fontSize: 19, fontWeight: 700, color: "#fff" }}>Tech Workforce Growth Dashboard</h1>
        <p style={{ fontSize: 11, color: "#555", marginTop: 4, fontFamily: "'JetBrains Mono'" }}>BLS 2024\u20132034 \u00b7 Industry reports \u00b7 US market</p>
      </div>

      <div style={{ padding: "0 20px 16px", display: "flex", gap: 6, flexWrap: "wrap" }}>
        {TABS.map((t, i) => <button key={t} className={`tb ${tab === i ? "a" : ""}`} onClick={() => setTab(i)}>{t}</button>)}
      </div>

      {/* TAB 0 */}
      {tab === 0 && (<div style={{ padding: "0 12px 20px" }}>
        <div style={{ padding: "0 8px 12px" }}><h2 style={{ fontSize: 15, fontWeight: 600, color: "#fff" }}>Fastest Growing Roles (2024\u20132034)</h2><p style={{ fontSize: 11, color: "#666", marginTop: 4 }}>Projected employment growth. Sources: BLS, ISC2, Gartner, WEF.</p></div>
        <div style={{ width: "100%", height: GROWTH_DATA.length * 32 }}><ResponsiveContainer><BarChart data={GROWTH_DATA} layout="vertical" margin={{ top: 0, right: 40, left: 0, bottom: 0 }}><XAxis type="number" domain={[0, 45]} tick={{ fill: "#555", fontSize: 10, fontFamily: "'JetBrains Mono'" }} axisLine={{ stroke: "#222" }} tickLine={false} tickFormatter={v => `${v}%`} /><YAxis type="category" dataKey="role" width={200} tick={{ fill: "#ccc", fontSize: 10.5 }} axisLine={false} tickLine={false} /><Tooltip content={<CTooltipBar />} cursor={{ fill: "rgba(255,255,255,0.03)" }} /><Bar dataKey="growth" radius={[0, 4, 4, 0]} maxBarSize={20}>{GROWTH_DATA.map((d, i) => <Cell key={i} fill={d.color} fillOpacity={0.75} />)}</Bar></BarChart></ResponsiveContainer></div>
        <div style={{ padding: "16px 8px 0", display: "flex", flexWrap: "wrap", gap: 8 }}>{[{l:"AI & ML",c:"#a855f7"},{l:"Cybersecurity",c:"#ff6b35"},{l:"Data Science",c:"#00d2ff"},{l:"Cloud & Infra",c:"#7b68ee"},{l:"Software Eng",c:"#e94560"},{l:"Finance",c:"#32cd32"},{l:"Consulting",c:"#00bfff"},{l:"Product",c:"#ff69b4"},{l:"Specialized",c:"#20b2aa"},{l:"IT Ops",c:"#50c878"},{l:"Networking",c:"#ffd700"}].map(x=><div key={x.l} style={{display:"flex",alignItems:"center",gap:4,fontSize:10,color:"#888"}}><div style={{width:8,height:8,borderRadius:2,background:x.c,opacity:.75}}/>{x.l}</div>)}</div>
      </div>)}

      {/* TAB 1 */}
      {tab === 1 && (<div style={{ padding: "0 12px 20px" }}>
        <div style={{ padding: "0 8px 12px" }}><h2 style={{ fontSize: 15, fontWeight: 600, color: "#fff" }}>Workforce Growth (2026\u20132036)</h2><p style={{ fontSize: 11, color: "#666", marginTop: 4 }}>Projected US workforce (thousands). Toggle categories.</p></div>
        <div style={{ padding: "0 8px 16px", display: "flex", flexWrap: "wrap", gap: 6 }}>{decadeCats.map(cat => { const d = DECADE_PROJECTIONS[cat]; const isOn = selectedCats.includes(cat); return <button key={cat} className="cc" onClick={() => setSelectedCats(p => p.includes(cat) ? p.filter(c => c !== cat) : [...p, cat])} style={{ background: isOn ? `${d.color}18` : "transparent", borderColor: isOn ? d.color : "rgba(255,255,255,0.1)", color: isOn ? d.color : "#555" }}>{cat.replace(" (Tech-Adjacent)","")}</button>; })}</div>
        <div style={{ width: "100%", height: 400 }}><ResponsiveContainer><AreaChart data={mergedDecadeData} margin={{ top: 10, right: 20, left: 10, bottom: 0 }}><CartesianGrid strokeDasharray="3 3" stroke="#1a1a2e" /><XAxis dataKey="year" tick={{ fill: "#666", fontSize: 11, fontFamily: "'JetBrains Mono'" }} axisLine={{ stroke: "#222" }} tickLine={false} /><YAxis tick={{ fill: "#555", fontSize: 10, fontFamily: "'JetBrains Mono'" }} axisLine={false} tickLine={false} tickFormatter={v => `${v}K`} /><Tooltip content={<CTooltipLine />} />{selectedCats.map(cat => { const d = DECADE_PROJECTIONS[cat]; return <Area key={cat} type="monotone" dataKey={cat} name={cat.replace(" (Tech-Adjacent)","")} stroke={d.color} fill={d.color} fillOpacity={0.08} strokeWidth={2} dot={false} activeDot={{ r: 4, fill: d.color }} />; })}</AreaChart></ResponsiveContainer></div>
        <div style={{ padding: "16px 8px 0", display: "grid", gridTemplateColumns: "repeat(auto-fill,minmax(190px,1fr))", gap: 8 }}>{decadeCats.sort((a, b) => DECADE_PROJECTIONS[b].growthRate - DECADE_PROJECTIONS[a].growthRate).map(cat => { const d = DECADE_PROJECTIONS[cat]; return <div key={cat} style={{ background: "rgba(255,255,255,0.02)", borderRadius: 8, padding: "10px 12px", borderLeft: `3px solid ${d.color}` }}><div style={{ fontSize: 10, fontWeight: 600, color: "#ddd" }}>{cat.replace(" (Tech-Adjacent)","")}</div><div style={{ fontFamily: "'JetBrains Mono'", fontSize: 16, fontWeight: 700, color: d.color, marginTop: 4 }}>+{(d.growthRate*100).toFixed(0)}%</div><div style={{ fontSize: 9, color: "#666", marginTop: 2 }}>{d.workers2026}K \u2192 {Math.round(d.workers2026*(1+d.growthRate))}K</div></div>; })}</div>
      </div>)}

      {/* TAB 2 */}
      {tab === 2 && (<div style={{ padding: "0 12px 20px" }}>
        <div style={{ padding: "0 8px 16px" }}>
          <h2 style={{ fontSize: 15, fontWeight: 600, color: "#fff" }}>Market Share by Category</h2>
          <p style={{ fontSize: 11, color: "#666", marginTop: 4, lineHeight: 1.5 }}>US workforce (2026 est.) split into pure tech roles and finance/consulting. Sources: BLS, ISC2, CyberSeek, CompTIA, LinkedIn.</p>
        </div>

        {/* TECH PIE */}
        <div style={{ padding: "0 8px 8px" }}>
          <div style={{ display: "flex", alignItems: "baseline", gap: 8, marginBottom: 4 }}>
            <h3 style={{ fontSize: 13, fontWeight: 700, color: "#fff" }}>Tech Roles</h3>
            <span style={{ fontFamily: "'JetBrains Mono'", fontSize: 11, color: "#e94560", fontWeight: 600 }}>~{(TECH_TOTAL / 1000).toFixed(1)}M</span>
            <span style={{ fontSize: 10, color: "#555" }}>professionals</span>
          </div>
        </div>
        <div style={{ width: "100%", height: 370 }}>
          <ResponsiveContainer>
            <PieChart>
              <Pie data={TECH_MARKET} cx="50%" cy="50%" innerRadius={50} outerRadius={120} paddingAngle={2} dataKey="value" stroke="#0a0a14" strokeWidth={2}
                label={renderColoredLabel} labelLine={{ stroke: "#333", strokeWidth: 1 }}>
                {TECH_MARKET.map((d, i) => <Cell key={i} fill={d.color} />)}
              </Pie>
              <Tooltip content={({ active, payload }) => {
                if (!active || !payload?.length) return null;
                const d = payload[0].payload;
                return (<div style={{ background: "#1a1a2e", border: "1px solid #333", borderRadius: 8, padding: "10px 14px", fontSize: 12, color: "#ddd" }}>
                  <div style={{ fontWeight: 600, color: "#fff", marginBottom: 4 }}>{d.name}</div>
                  <div style={{ fontFamily: "'JetBrains Mono'" }}><span style={{ color: d.color, fontWeight: 700 }}>{d.value.toLocaleString()}K</span> workers</div>
                  <div style={{ color: "#888", marginTop: 2 }}>{((d.value / TECH_TOTAL) * 100).toFixed(1)}% of tech workforce</div>
                </div>);
              }} />
            </PieChart>
          </ResponsiveContainer>
        </div>
        {/* Tech breakdown list */}
        <div style={{ padding: "4px 8px 24px" }}>
          {TECH_MARKET.map(d => {
            const pct = ((d.value / TECH_TOTAL) * 100).toFixed(1);
            const barW = (d.value / TECH_MARKET[0].value) * 100;
            return (<div key={d.name} style={{ display: "flex", alignItems: "center", gap: 10, padding: "7px 0", borderBottom: "1px solid rgba(255,255,255,0.03)" }}>
              <div style={{ width: 10, height: 10, borderRadius: 3, background: d.color, flexShrink: 0 }} />
              <div style={{ flex: 1, minWidth: 0 }}>
                <div style={{ fontSize: 11.5, fontWeight: 500, color: "#ddd" }}>{d.name}</div>
                <div style={{ height: 4, background: "rgba(255,255,255,0.04)", borderRadius: 2, marginTop: 4 }}>
                  <div style={{ height: "100%", borderRadius: 2, background: d.color, opacity: 0.65, width: `${barW}%` }} />
                </div>
              </div>
              <div style={{ textAlign: "right", flexShrink: 0 }}>
                <div style={{ fontFamily: "'JetBrains Mono'", fontSize: 12, fontWeight: 600, color: "#fff" }}>{d.value.toLocaleString()}K</div>
                <div style={{ fontSize: 9, color: "#666" }}>{pct}%</div>
              </div>
            </div>);
          })}
        </div>

        {/* FINANCE & CONSULTING PIE */}
        <div style={{ padding: "0 8px 8px", borderTop: "1px solid rgba(255,255,255,0.06)", paddingTop: 20 }}>
          <div style={{ display: "flex", alignItems: "baseline", gap: 8, marginBottom: 4 }}>
            <h3 style={{ fontSize: 13, fontWeight: 700, color: "#fff" }}>Finance & Consulting</h3>
            <span style={{ fontFamily: "'JetBrains Mono'", fontSize: 11, color: "#32cd32", fontWeight: 600 }}>~{(BIZ_TOTAL / 1000).toFixed(1)}M</span>
            <span style={{ fontSize: 10, color: "#555" }}>professionals</span>
          </div>
        </div>
        <div style={{ width: "100%", height: 280 }}>
          <ResponsiveContainer>
            <PieChart>
              <Pie data={BIZ_MARKET} cx="50%" cy="50%" innerRadius={40} outerRadius={90} paddingAngle={3} dataKey="value" stroke="#0a0a14" strokeWidth={2}
                label={renderColoredLabel} labelLine={{ stroke: "#333", strokeWidth: 1 }}>
                {BIZ_MARKET.map((d, i) => <Cell key={i} fill={d.color} />)}
              </Pie>
              <Tooltip content={({ active, payload }) => {
                if (!active || !payload?.length) return null;
                const d = payload[0].payload;
                return (<div style={{ background: "#1a1a2e", border: "1px solid #333", borderRadius: 8, padding: "10px 14px", fontSize: 12, color: "#ddd" }}>
                  <div style={{ fontWeight: 600, color: "#fff", marginBottom: 4 }}>{d.name}</div>
                  <div style={{ fontFamily: "'JetBrains Mono'" }}><span style={{ color: d.color, fontWeight: 700 }}>{d.value.toLocaleString()}K</span> workers</div>
                  <div style={{ color: "#888", marginTop: 2 }}>{((d.value / BIZ_TOTAL) * 100).toFixed(1)}% of finance/consulting</div>
                </div>);
              }} />
            </PieChart>
          </ResponsiveContainer>
        </div>
        {/* Biz breakdown list */}
        <div style={{ padding: "4px 8px 16px" }}>
          {BIZ_MARKET.map(d => {
            const pct = ((d.value / BIZ_TOTAL) * 100).toFixed(1);
            const barW = (d.value / BIZ_MARKET[0].value) * 100;
            return (<div key={d.name} style={{ display: "flex", alignItems: "center", gap: 10, padding: "7px 0", borderBottom: "1px solid rgba(255,255,255,0.03)" }}>
              <div style={{ width: 10, height: 10, borderRadius: 3, background: d.color, flexShrink: 0 }} />
              <div style={{ flex: 1, minWidth: 0 }}>
                <div style={{ fontSize: 11.5, fontWeight: 500, color: "#ddd" }}>{d.name}</div>
                <div style={{ height: 4, background: "rgba(255,255,255,0.04)", borderRadius: 2, marginTop: 4 }}>
                  <div style={{ height: "100%", borderRadius: 2, background: d.color, opacity: 0.65, width: `${barW}%` }} />
                </div>
              </div>
              <div style={{ textAlign: "right", flexShrink: 0 }}>
                <div style={{ fontFamily: "'JetBrains Mono'", fontSize: 12, fontWeight: 600, color: "#fff" }}>{d.value.toLocaleString()}K</div>
                <div style={{ fontSize: 9, color: "#666" }}>{pct}%</div>
              </div>
            </div>);
          })}
        </div>

        {/* Combined stat */}
        <div style={{ display: "flex", gap: 12, padding: "8px 8px 0" }}>
          <div style={{ flex: 1, background: "rgba(233,69,96,0.06)", borderRadius: 10, padding: "14px 16px", border: "1px solid rgba(233,69,96,0.15)", textAlign: "center" }}>
            <div style={{ fontSize: 9, color: "#888", textTransform: "uppercase", letterSpacing: 0.8 }}>Pure Tech</div>
            <div style={{ fontFamily: "'JetBrains Mono'", fontSize: 22, fontWeight: 700, color: "#e94560", marginTop: 4 }}>~{(TECH_TOTAL / 1000).toFixed(1)}M</div>
            <div style={{ fontSize: 10, color: "#555", marginTop: 2 }}>{TECH_MARKET.length} categories</div>
          </div>
          <div style={{ flex: 1, background: "rgba(50,205,50,0.06)", borderRadius: 10, padding: "14px 16px", border: "1px solid rgba(50,205,50,0.15)", textAlign: "center" }}>
            <div style={{ fontSize: 9, color: "#888", textTransform: "uppercase", letterSpacing: 0.8 }}>Finance & Consulting</div>
            <div style={{ fontFamily: "'JetBrains Mono'", fontSize: 22, fontWeight: 700, color: "#32cd32", marginTop: 4 }}>~{(BIZ_TOTAL / 1000).toFixed(1)}M</div>
            <div style={{ fontSize: 10, color: "#555", marginTop: 2 }}>{BIZ_MARKET.length} categories</div>
          </div>
          <div style={{ flex: 1, background: "rgba(255,255,255,0.02)", borderRadius: 10, padding: "14px 16px", border: "1px solid rgba(255,255,255,0.06)", textAlign: "center" }}>
            <div style={{ fontSize: 9, color: "#888", textTransform: "uppercase", letterSpacing: 0.8 }}>Combined</div>
            <div style={{ fontFamily: "'JetBrains Mono'", fontSize: 22, fontWeight: 700, color: "#fff", marginTop: 4 }}>~{(TOTAL_WORKERS / 1000).toFixed(1)}M</div>
            <div style={{ fontSize: 10, color: "#555", marginTop: 2 }}>total workforce</div>
          </div>
        </div>
      </div>)}

      {/* TAB 3: CAREER RANKING */}
      {tab === 3 && (<div style={{ padding: "0 12px 20px" }}>
        <div style={{ padding: "0 8px 16px" }}>
          <h2 style={{ fontSize: 15, fontWeight: 600, color: "#fff" }}>Career Path Ranking</h2>
          <p style={{ fontSize: 11, color: "#666", marginTop: 4, lineHeight: 1.6 }}>
            Scored 1\u20135 across six dimensions. Composite weighted: Stability 20%, Entry Ease 20%, Growth 18%, Salary 15%, Low Competition 15%, Entry Opportunity 12%. Tap cards to expand.
          </p>
        </div>

        {/* Radar */}
        <div style={{ padding: "0 8px 8px" }}>
          <div style={{ fontSize: 11, fontWeight: 600, color: "#888", marginBottom: 8 }}>Radar Compare (tap 2\u20133):</div>
          <div style={{ display: "flex", flexWrap: "wrap", gap: 5 }}>
            {RANKING_SCORED.map((d, i) => { const on = radarPicks.includes(i); return <button key={d.name} className="cc" onClick={() => toggleRadar(i)} style={{ background: on ? `${d.color}20` : "transparent", borderColor: on ? d.color : "rgba(255,255,255,0.1)", color: on ? d.color : "#555" }}>{d.name}</button>; })}
          </div>
        </div>
        {radarPicks.length >= 2 && (
          <div style={{ width: "100%", height: 280, marginBottom: 12 }}>
            <ResponsiveContainer>
              <RadarChart data={radarData} margin={{ top: 10, right: 30, bottom: 10, left: 30 }}>
                <PolarGrid stroke="#1f1f35" />
                <PolarAngleAxis dataKey="subject" tick={{ fill: "#999", fontSize: 9.5 }} />
                <PolarRadiusAxis domain={[0, 5]} tick={{ fill: "#444", fontSize: 9 }} axisLine={false} />
                {radarPicks.map(idx => { const d = RANKING_SCORED[idx]; return d ? <Radar key={d.name} name={d.name} dataKey={d.name} stroke={d.color} fill={d.color} fillOpacity={0.1} strokeWidth={2} dot={{ r: 3, fill: d.color }} /> : null; })}
              </RadarChart>
            </ResponsiveContainer>
            <div style={{ display: "flex", justifyContent: "center", gap: 16 }}>
              {radarPicks.map(idx => { const d = RANKING_SCORED[idx]; return d ? <div key={d.name} style={{ display: "flex", alignItems: "center", gap: 5, fontSize: 10.5, color: d.color }}><div style={{ width: 12, height: 3, background: d.color, borderRadius: 2 }} />{d.name}</div> : null; })}
            </div>
          </div>
        )}

        {/* Cards */}
        <div style={{ display: "flex", flexDirection: "column", gap: 10, padding: "8px 4px 0" }}>
          {RANKING_SCORED.map((d, idx) => {
            const open = expandedRank === idx;
            return (
              <div key={d.name} className="rc" onClick={() => setExpandedRank(open ? -1 : idx)}
                style={{ background: open ? "rgba(255,255,255,0.025)" : "rgba(255,255,255,0.015)", borderColor: open ? `${d.color}40` : undefined }}>
                <div style={{ padding: "14px 16px", display: "flex", alignItems: "center", gap: 12 }}>
                  <div style={{ width: 34, height: 34, borderRadius: 8, background: `${d.color}20`, display: "flex", alignItems: "center", justifyContent: "center", fontFamily: "'JetBrains Mono'", fontSize: 14, fontWeight: 700, color: d.color, flexShrink: 0 }}>#{idx + 1}</div>
                  <div style={{ flex: 1 }}>
                    <div style={{ fontSize: 14, fontWeight: 700, color: "#fff" }}>{d.name}</div>
                    <div style={{ fontSize: 11, color: d.color, fontWeight: 500, marginTop: 1 }}>{d.verdict}</div>
                  </div>
                  <GradeCircle score={d.composite} />
                </div>
                <div style={{ padding: "0 16px 12px", display: "grid", gridTemplateColumns: "1fr 1fr", gap: "5px 16px" }}>
                  {DIMS.map(dim => (<div key={dim.key}><div style={{ fontSize: 9, color: "#666", marginBottom: 2 }}>{dim.icon} {dim.label}</div><ScoreBar value={d[dim.key]} /></div>))}
                </div>
                {open && (
                  <div style={{ padding: "0 16px 16px", borderTop: "1px solid rgba(255,255,255,0.04)", paddingTop: 12 }}>
                    <p style={{ fontSize: 12, color: "#bbb", lineHeight: 1.7, marginBottom: 12 }}>{d.why}</p>
                    <div style={{ display: "grid", gridTemplateColumns: "1fr 1fr", gap: 10 }}>
                      <div style={{ background: "rgba(255,255,255,0.03)", borderRadius: 8, padding: "10px 12px" }}>
                        <div style={{ fontSize: 9, color: "#666", textTransform: "uppercase", letterSpacing: 0.5, marginBottom: 4 }}>🚪 Suggested Entry Path</div>
                        <div style={{ fontSize: 11, color: "#ddd", lineHeight: 1.6 }}>{d.entryPath}</div>
                      </div>
                      <div style={{ background: "rgba(255,255,255,0.03)", borderRadius: 8, padding: "10px 12px" }}>
                        <div style={{ fontSize: 9, color: "#666", textTransform: "uppercase", letterSpacing: 0.5, marginBottom: 4 }}>⏱ Prep Time</div>
                        <div style={{ fontSize: 11, color: "#ddd", lineHeight: 1.6 }}>{d.prepHours}</div>
                      </div>
                      <div style={{ background: "rgba(255,255,255,0.03)", borderRadius: 8, padding: "10px 12px" }}>
                        <div style={{ fontSize: 9, color: "#666", textTransform: "uppercase", letterSpacing: 0.5, marginBottom: 4 }}>🎯 Time to First Role</div>
                        <div style={{ fontSize: 11, color: "#ddd", lineHeight: 1.6 }}>{d.timeToEntry}</div>
                      </div>
                      <div style={{ background: "rgba(255,255,255,0.03)", borderRadius: 8, padding: "10px 12px" }}>
                        <div style={{ fontSize: 9, color: "#666", textTransform: "uppercase", letterSpacing: 0.5, marginBottom: 4 }}>🚀 Level-Up Trajectory</div>
                        <div style={{ fontSize: 11, color: "#ddd", lineHeight: 1.6 }}>{d.levelUpNotes}</div>
                      </div>
                    </div>
                  </div>
                )}
              </div>
            );
          })}
        </div>

        {/* Weights */}
        <div style={{ padding: "20px 8px 0" }}>
          <div style={{ background: "rgba(255,255,255,0.02)", borderRadius: 10, padding: "14px 16px", border: "1px solid rgba(255,255,255,0.04)" }}>
            <div style={{ fontSize: 11, fontWeight: 600, color: "#888", marginBottom: 8 }}>How the composite score works</div>
            <div style={{ display: "flex", flexWrap: "wrap", gap: 6 }}>
              {Object.entries(WEIGHTS).map(([k, w]) => { const dim = DIMS.find(d => d.key === k); return <div key={k} style={{ background: "rgba(255,255,255,0.03)", borderRadius: 6, padding: "4px 10px", fontSize: 10, color: "#aaa" }}>{dim?.icon} {dim?.label}: <span style={{ fontFamily: "'JetBrains Mono'", fontWeight: 600, color: "#ddd" }}>{(w*100).toFixed(0)}%</span></div>; })}
            </div>
            <p style={{ fontSize: 10, color: "#555", marginTop: 8, lineHeight: 1.6 }}>Weights balanced across 8 dimensions. Accessibility factors (entry ease, low prep time, entry opportunity) = 37%, trajectory factors (growth, level-up, salary) = 38%, risk factors (stability, low competition) = 25%. A career path is only worth pursuing if you can both get in and keep moving up.</p>
          </div>
        </div>
      </div>)}

      <div style={{ padding: "20px", borderTop: "1px solid rgba(255,255,255,0.04)", fontSize: 9, color: "#333", lineHeight: 1.8 }}>
        <strong style={{ color: "#444" }}>Sources:</strong> BLS 2024\u20132034, ISC2 2025, Gartner, CompTIA, WEF Future of Jobs 2025, LinkedIn Economic Graph, Motion Recruitment 2026. Rankings reflect editorial judgment combining quantitative data with industry consensus.
      </div>
    </div>
  );
}

