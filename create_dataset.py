import pandas as pd
import numpy as np

# =============== DATASET GENERATION (PASS/FAIL ONLY BY FINAL SCORE) ===============
rows = 6000
np.random.seed(42)

# -------- Generate Base Features ----------
previous = np.clip(np.random.normal(55,30,rows),0,100)
hours = np.clip(np.random.normal(3.5,1.5,rows),0,10)
attendance = np.clip(np.random.normal(65,15,rows),0,100)
assignments = np.clip(np.random.normal(6.5,3,rows),0,12).astype(int)
sleep = np.clip(np.random.normal(7,1.5,rows),1,10)
participation_cat = np.random.choice(["Low","Medium","High"],size=rows,p=[0.20,0.50,0.30])

# Participation numeric mapping
part_map = {"Low":30,"Medium":60,"High":90}
participation_num = np.array([part_map[p] for p in participation_cat])

# -------- Normalize to 0–100 Scale ----------
norm_prev = previous
norm_att = attendance
norm_assign = (assignments/12)*100
norm_hours = (hours/10)*100
norm_sleep = ((sleep-3)/7)*100

# -------- FINAL SCORE USING WEIGHTS ----------
final_score = (
    norm_prev*0.55 +
    norm_hours*0.20 +
    norm_att*0.12 +
    norm_assign*0.05 +
    participation_num*0.04 +
    norm_sleep*0.04 +
    np.random.normal(0,2,rows)   # small noise for reality
)

# -------- Improvement & Decline ----------
for i in range(rows):
    if attendance[i] < 45: final_score[i] -= np.random.uniform(3,8)
    if hours[i] < 1.5: final_score[i] -= np.random.uniform(2,5)

    if hours[i] > 5: final_score[i] += np.random.uniform(2,5)
    if assignments[i] > 8: final_score[i] += np.random.uniform(2,5)
    if attendance[i] > 80: final_score[i] += np.random.uniform(3,8)

# Keep scores valid
final_score = np.clip(final_score,0,100).round(1)

# --------  PASS/FAIL LOGIC  ----------
pass_fail = (final_score >= 40).astype(int)

# -------- Build CSV ----------
df = pd.DataFrame({
    "Previous_Score": previous.round(1),
    "Hours_Studied": hours.round(2),
    "Attendance": attendance.round(1),
    "Assignments_Completed": assignments,
    "Sleep_Hours": sleep.round(1),
    "Participation": participation_cat,
    "Final_Score": final_score,
    "Pass_Fail": pass_fail
})

df.to_csv("data/raw_dataset.csv",index=False)
print("CSV Generated Successfully: raw_data.csv")
