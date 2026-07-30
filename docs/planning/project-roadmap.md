# AI Workforce Analytics Platform — Project Roadmap
### Employee Attrition Prediction System (Resume-Grade SaaS Build)

---

## 1. High-Level Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                         FRONTEND (Vercel)                       │
│   React + TypeScript + Tailwind + shadcn/ui + Recharts           │
│   Dashboard | Prediction | Batch Upload | Analytics | Insights   │
└───────────────────────────┬───────────────────────────────────────┘
                            │ REST (JSON) over HTTPS
┌───────────────────────────▼───────────────────────────────────────┐
│                        BACKEND (Render/Railway)                  │
│   FastAPI (Python) — Auth, Validation, Business Logic             │
│   ┌───────────────┐   ┌────────────────┐   ┌────────────────┐    │
│   │ Prediction API │   │ Batch API      │   │ Recommendation │    │
│   └───────┬────────┘   └───────┬────────┘   │ Engine (rules) │    │
│           │                    │            └────────────────┘    │
│   ┌───────▼────────────────────▼────────┐                        │
│   │ ML Inference Layer (joblib/pickle)   │                        │
│   │  Model + Preprocessing Pipeline      │                        │
│   │  + SHAP Explainer (cached)           │                        │
│   └───────────────────────────────────────┘                        │
└───────────────────────────┬───────────────────────────────────────┘
                            │
┌───────────────────────────▼───────────────────────────────────────┐
│                     DATABASE (PostgreSQL)                        │
│   Employees | Predictions | Users | Departments | Reports         │
└─────────────────────────────────────────────────────────────────┘

Offline / Training side (not user-facing, runs in notebooks/scripts):
Raw Data → Cleaning → EDA → Feature Engineering → Training →
Hyperparameter Tuning → Evaluation → SHAP → Serialized Model Artifact
```

**Why this shape, not a single Flask app with everything inline?**
Separating the *training pipeline* (offline, run occasionally) from the *inference layer* (online, runs on every request) mirrors how real ML systems work. You train once, version the artifact, and the API just loads and serves it — this is the core idea behind "training/serving skew" avoidance and is a talking point interviewers actually probe for.

---

## 2. Folder Structure

```
attrition-analytics-platform/
├── ml/
│   ├── notebooks/
│   │   ├── 01_eda.ipynb
│   │   ├── 02_preprocessing.ipynb
│   │   ├── 03_model_training.ipynb
│   │   └── 04_explainability.ipynb
│   ├── src/
│   │   ├── data_loader.py
│   │   ├── preprocessing.py
│   │   ├── feature_engineering.py
│   │   ├── train.py
│   │   ├── evaluate.py
│   │   └── explain.py
│   ├── artifacts/
│   │   ├── model.pkl
│   │   ├── preprocessor.pkl
│   │   └── shap_explainer.pkl
│   └── data/
│       ├── raw/
│       └── processed/
│
├── backend/
│   ├── app/
│   │   ├── main.py
│   │   ├── api/
│   │   │   ├── routes_predict.py
│   │   │   ├── routes_batch.py
│   │   │   ├── routes_auth.py
│   │   │   └── routes_health.py
│   │   ├── core/
│   │   │   ├── config.py
│   │   │   └── security.py
│   │   ├── models/          # Pydantic schemas
│   │   ├── db/
│   │   │   ├── models.py    # SQLAlchemy ORM
│   │   │   └── session.py
│   │   ├── services/
│   │   │   ├── inference_service.py
│   │   │   └── recommendation_engine.py
│   │   └── tests/
│   ├── requirements.txt
│   ├── Dockerfile
│   └── alembic/              # DB migrations
│
├── frontend/
│   ├── src/
│   │   ├── pages/
│   │   │   ├── Dashboard.tsx
│   │   │   ├── Prediction.tsx
│   │   │   ├── BatchUpload.tsx
│   │   │   ├── Analytics.tsx
│   │   │   └── ModelInsights.tsx
│   │   ├── components/
│   │   ├── hooks/
│   │   ├── lib/api.ts
│   │   └── types/
│   ├── package.json
│   └── vite.config.ts
│
├── docs/
│   ├── architecture.md
│   ├── api-docs.md
│   ├── er-diagram.png
│   ├── model-report.md
│   └── deployment-guide.md
│
├── docker-compose.yml
└── README.md
```

---

## 3. Timeline (Solo, ~8–12 hrs/week pace)

| Phase | Focus | Est. Time |
|---|---|---|
| 1 | Planning & Architecture | 3–4 hrs |
| 2–3 | Dataset Analysis + EDA | 8–10 hrs |
| 4 | Preprocessing | 5–6 hrs |
| 5 | Model Building | 8–10 hrs |
| 6 | Hyperparameter Tuning | 4–5 hrs |
| 7 | Explainability (SHAP) | 5–6 hrs |
| 8 | Backend API | 8–10 hrs |
| 9 | Frontend Dashboard | 12–15 hrs |
| 10 | Visualizations | 5–6 hrs |
| 11 | Recommendation Engine | 3–4 hrs |
| 12 | Auth & Roles | 5–6 hrs |
| 13 | Database Schema | 4–5 hrs |
| 14 | Deployment & CI/CD | 6–8 hrs |
| 15 | Documentation | 4–5 hrs |
| **Total** | | **~85–100 hrs** (~6–8 weeks part-time) |

If this is for a hackathon (24–48 hrs), you'd compress to Phases 1, 2, 4, 5, 7 (skip tuning depth), 8, and a lightweight version of 9 — cut auth/roles and full CI/CD entirely. I can give you that compressed version separately if you want it.

---

## 4. Milestones

### Phase 1 — Project Planning
**Objective:** Lock scope before writing any code.
**Why it matters:** Most student projects fail not from bad code but from scope creep — you'll otherwise rebuild the DB schema three times.
**Deliverables:** Scope doc, functional/non-functional requirements, 3–5 user stories (Admin/HR/Manager), tech stack justification doc.
**Skills learned:** Requirements engineering, system design thinking.
**Common mistakes:** Jumping straight to model training without defining what "attrition risk" means to the end user (a probability? a category? both?).
**Best practice:** Write user stories as "As an HR manager, I want to see which department has the highest attrition risk so that I can allocate retention budget."
**Time:** 3–4 hrs.

### Phase 2–3 — Dataset Analysis & EDA
**Objective:** Understand the IBM HR Analytics dataset (or equivalent) at a business level, not just statistically.
**Why it matters:** SHAP explanations are meaningless if you don't understand what `OverTime` or `JobInvolvement` mean in HR context — you won't be able to translate model output into recommendations later.
**Deliverables:** `01_eda.ipynb` with: attrition distribution, department-wise attrition, salary bands vs attrition, age distribution, overtime impact, correlation heatmap — each with a 2–3 sentence business interpretation, not just a plot.
**Skills learned:** pandas, seaborn/matplotlib, statistical reasoning, class imbalance diagnosis.
**Common mistakes:** Treating this dataset's ~16% attrition rate as "fine" without addressing imbalance later; dropping "Over18"/"EmployeeCount" columns without checking they're constant first.
**Best practice:** For every chart, write down: "what would an HR person conclude from this, and is that conclusion statistically sound?"
**Time:** 8–10 hrs.

### Phase 4 — Data Preprocessing
**Objective:** Build a leak-free, reproducible preprocessing pipeline.
**Why it matters:** Data leakage (e.g., scaling before train/test split) is the #1 reason portfolio ML metrics don't reproduce in production — reviewers who know ML will check for this.
**Deliverables:** `preprocessing.py` using `sklearn.Pipeline` + `ColumnTransformer` (OneHotEncoder for categoricals, StandardScaler for numerics), saved as `preprocessor.pkl`.
**Skills learned:** sklearn Pipelines, encoding strategies, train/test discipline.
**Common mistakes:** Fitting the scaler/encoder on the full dataset instead of only `X_train`.
**Best practice:** Wrap everything in a single `Pipeline` object so the exact same transform runs at inference time — this is what prevents train/serve skew.
**Time:** 5–6 hrs.

### Phase 5 — Model Building
**Objective:** Train and compare Logistic Regression, Decision Tree, Random Forest, XGBoost, LightGBM.
**Why it matters:** A comparison table demonstrates you understand trade-offs (interpretability vs. performance), not just that you can call `.fit()`.
**Deliverables:** Comparison table (Accuracy, Precision, Recall, F1, ROC-AUC, 5-fold CV) + confusion matrices.
**Skills learned:** Model selection, cross-validation, metric literacy (why Recall matters more than Accuracy here — missing a real attrition case is costlier than a false alarm).
**Common mistakes:** Reporting only accuracy on an imbalanced dataset (a model predicting "no attrition" always gets ~84% accuracy and is useless).
**Best practice:** Pick your primary metric (likely Recall or F1 for the minority class) *before* training, and justify it in writing.
**Time:** 8–10 hrs.

### Phase 6 — Hyperparameter Optimization
**Objective:** Tune your top 1–2 models using `RandomizedSearchCV` (and `GridSearchCV` for final refinement).
**Why it matters:** Shows you understand the compute/search-space trade-off — Grid search on XGBoost's full space is computationally naive.
**Deliverables:** Best params + before/after metric comparison.
**Skills learned:** Search strategies, cross-validated tuning, avoiding overfitting to the validation fold.
**Common mistakes:** Tuning on the test set (this silently invalidates your final evaluation).
**Best practice:** Reserve test set only for the final, one-time evaluation.
**Time:** 4–5 hrs.

### Phase 7 — Model Explainability (SHAP)
**Objective:** Generate global and local explanations.
**Why it matters:** This is the differentiator — "black box that predicts attrition" is a school project; "explains *why* Priya is at risk and what to do about it" is a product.
**Deliverables:** SHAP summary plot (global feature importance), waterfall plot for individual predictions, written translation of SHAP output into HR language.
**Skills learned:** SHAP values, TreeExplainer, communicating ML output to non-technical stakeholders.
**Common mistakes:** Showing raw SHAP plots to "HR" personas without translation — always pair each SHAP output with a plain-English sentence.
**Best practice:** Cache the explainer object at model-training time so the API doesn't recompute it per request.
**Time:** 5–6 hrs.

### Phase 8 — Backend (FastAPI)
**Objective:** Production-quality REST API serving predictions.
**Why it matters:** This is where "notebook project" becomes "deployable system."
**Deliverables:** `/predict`, `/predict/batch`, `/health` endpoints; Pydantic request/response validation; structured error handling (422 vs 500 distinctions).
**Skills learned:** FastAPI, Pydantic schemas, async I/O basics, API design.
**Common mistakes:** Loading the model fresh on every request instead of once at startup (`app.state` or a singleton).
**Best practice:** Load model + preprocessor + SHAP explainer once in a startup event; validate input schema strictly so malformed employee records don't silently produce garbage predictions.
**Time:** 8–10 hrs.

### Phase 9 — Frontend
**Objective:** Build Dashboard, Prediction, Batch Upload, Analytics, Model Insights, About pages.
**Why it matters:** This is what a recruiter actually clicks through — polish here has outsized ROI.
**Deliverables:** Responsive React app with shadcn/ui components, Recharts visualizations, API integration via a typed `lib/api.ts` client.
**Skills learned:** React + TypeScript patterns, component composition, chart libraries, responsive design.
**Common mistakes:** No loading/error states — a demo that shows a blank screen on API failure looks unfinished.
**Best practice:** Design the loading/empty/error state for every page *before* the happy path.
**Time:** 12–15 hrs.

### Phase 10 — Visualization
**Objective:** Risk gauge, department risk chart, employee distribution, prediction history, trend analysis.
**Deliverables:** Interactive Recharts components fed by backend aggregation endpoints.
**Skills learned:** Data aggregation for viz, chart library composition.
**Common mistakes:** Doing aggregation client-side on large datasets instead of letting the backend/DB do it.
**Time:** 5–6 hrs.

### Phase 11 — Recommendation Engine
**Objective:** Rule-based, explainable retention recommendations tied to SHAP drivers.
**Deliverables:** `recommendation_engine.py` mapping top SHAP features → actionable text (e.g., high `OverTime` contribution → "Recommend workload rebalancing").
**Skills learned:** Turning model output into business action — a genuinely underrated skill.
**Common mistakes:** Hardcoding recommendations disconnected from the actual SHAP values for that specific employee (looks fake in a demo).
**Time:** 3–4 hrs.

### Phase 12 — Authentication & Roles
**Objective:** Admin / HR / Manager roles with different dashboard permissions.
**Deliverables:** JWT-based auth, role-based route guards on both frontend and backend.
**Skills learned:** Auth flows, RBAC (role-based access control).
**Common mistakes:** Enforcing roles only in the frontend — always re-check permissions server-side.
**Time:** 5–6 hrs.

### Phase 13 — Database
**Objective:** Design a normalized schema: Employees, Predictions, Users, Departments, History, Reports.
**Deliverables:** ER diagram, SQLAlchemy models, Alembic migrations.
**Skills learned:** Relational schema design, migrations discipline.
**Common mistakes:** Storing prediction results as loose JSON blobs instead of proper columns — makes analytics queries painful later.
**Time:** 4–5 hrs.

### Phase 14 — Deployment
**Objective:** Ship frontend (Vercel), backend (Render/Railway), DB (managed Postgres), containerized via Docker.
**Deliverables:** `Dockerfile`, `docker-compose.yml`, environment variable management, basic CI (GitHub Actions running tests on push).
**Skills learned:** Containerization, env-based config, CI basics.
**Common mistakes:** Committing `.env` files or hardcoding secrets in the repo.
**Time:** 6–8 hrs.

### Phase 15 — Documentation
**Objective:** README, architecture diagram, API docs, ER diagram, model report, deployment guide.
**Why it matters:** This is often the first (and sometimes only) thing a recruiter or hackathon judge reads — treat it as a deliverable, not an afterthought.
**Deliverables:** Polished README with screenshots/GIFs, `docs/` folder with the above.
**Time:** 4–5 hrs.

---

## 5. Learning Objectives (Cumulative)

- End-to-end ML lifecycle: EDA → preprocessing → training → tuning → explainability
- Leak-free pipeline design with `sklearn.Pipeline`
- Explainable AI with SHAP, and translating it for non-technical users
- Production API design with FastAPI (validation, error handling, startup-time model loading)
- Full-stack integration between a typed React frontend and a Python ML backend
- Relational schema design for an ML-driven product
- Auth/RBAC fundamentals
- Docker-based deployment and basic CI

---

## 6. Risks

| Risk | Mitigation |
|---|---|
| Scope creep (trying to build all "future scalability" ideas at once) | Ship Phases 1–11 as v1; treat 12–15 as v1.1; treat LLM/chatbot ideas as v2 |
| Class imbalance leading to misleading accuracy | Commit to Recall/F1 as primary metric from Phase 5 onward |
| SHAP compute cost at inference time | Precompute/cache explainer; don't recompute per request |
| Frontend polish taking longer than expected | Time-box Phase 9; use shadcn/ui defaults rather than custom design system |
| Deployment cold-start on free tiers (Render) | Mention this explicitly in docs as a known limitation, not a bug |

---

## 7. Final Project Vision

A deployed, demoable SaaS-style tool where an HR manager logs in, uploads employee data (or picks one from a list), sees a plain-English risk explanation ("this employee is high-risk primarily due to overtime and low job satisfaction"), and gets a concrete retention recommendation — all backed by a real, evaluated ML model with documented metrics and an honest limitations section. Future direction: LLM-powered natural language querying over the analytics ("which department needs attention this quarter?"), scheduled email reports, and model retraining pipelines (MLOps direction) — good talking points for interviews even if not fully built.

---

**Next step:** We start Phase 1 in detail — scope doc, user stories, and tech stack justification — before touching the dataset. Let me know when you're ready and I'll walk through it as a mini sprint, exactly as outlined above.
