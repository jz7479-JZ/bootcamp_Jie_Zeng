# Project Title
**Stage:** Problem Framing & Scoping (Stage 01)  
**Title:** Image-to-LaTeX Conversion Tool

## Problem Statement
In academic research, education, and technical publishing, mathematical formulas often appear in image form (scanned documents, lecture slides, handwritten notes). These images are not editable and cannot be directly processed by LaTeX-based typesetting systems. The problem is to create a reliable method for converting mathematical formulas from images into accurate LaTeX code. This would save time for researchers, educators, and students, and improve the accuracy and efficiency of producing technical documents.

## Stakeholder & User
- **Primary stakeholders:** Researchers, educators, students in STEM fields, and publishers who frequently deal with mathematical documents.  
- **End users:** Individuals who need to quickly and accurately convert formula images into LaTeX code for papers, assignments, or presentations.  
- **Workflow context:** Users upload or capture an image, the system processes it, and outputs LaTeX code that can be pasted into Overleaf, TeX editors, or Markdown documents.

## Useful Answer & Decision
- **Type:** Predictive / Artifact  
- **Metric:** Conversion accuracy (LaTeX correctness rate), processing time per formula.  
- **Artifact:** A software tool (script, web app, or notebook) that accepts formula images and outputs LaTeX code.

## Assumptions & Constraints
- Sufficient training data of formula images and their corresponding LaTeX.  
- Ability to process common formats (PNG, JPG, PDF snapshots).  
- Reasonable processing time (under 5 seconds per formula).  
- Compliance with licensing for datasets and libraries used.

## Known Unknowns / Risks
- OCR model’s ability to handle complex multi-line equations.  
- Handling handwritten vs. printed formulas.  
- Accuracy drop for noisy or low-resolution images.  
- Risk of LaTeX syntax errors requiring manual correction.

## Lifecycle Mapping
Goal → Stage → Deliverable  
- Build a reliable formula recognition model → Problem Framing & Scoping (Stage 01) → Scoping paragraph, repo setup, stakeholder artifact  
- Collect and preprocess dataset → Data Collection (Stage 02) → Clean labeled dataset  
- Train and evaluate recognition model → Modeling (Stage 03) → Trained model with metrics report

## Repo Plan
- **/data** – Stores raw and cleaned formula images with corresponding LaTeX labels.  
- **/src** – Python scripts for data preprocessing, model training, inference, and result validation.  
- **/notebooks** – Jupyter notebooks for exploratory analysis, prototyping, and testing.  
- **/docs** – Project documentation, reports, and visualizations.  
- **Cadence for updates** - updates weekly.
