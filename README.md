# 🧠 پروژه تحلیل پیش‌بینانه انطباق سازمانی کارکنان (Person-Organization Fit Predictor)

این پروژه با هدف ارزیابی و پیش‌بینی میزان سازگاری کارکنان با فرهنگ سازمانی، محیط کاری و سبک مدیریتی شرکت طراحی شده است. در این پروژه از مفاهیم **روان‌شناسی سازمانی، تحلیل داده و یادگیری ماشین** برای سنجش میزان **انطباق فرد با سازمان (Person-Organization Fit)** استفاده شده است.

هدف اصلی پروژه، کمک به واحد منابع انسانی در شناسایی کارکنانی است که ممکن است در محیط فعلی خود عملکرد مطلوبی نداشته باشند، احساس نارضایتی کنند یا در معرض ترک سازمان قرار گیرند.

---

## 🏢 سناریوی بیزنسی پروژه (Business Scenario)

شرکت فناوری **ساینپس‌تک (SynapseTech)** در سال‌های اخیر با چالشی پنهان روبه‌رو شده است. با وجود جذب نیروهای متخصص و ارائه مزایای رقابتی، برخی کارکنان پس از مدت کوتاهی دچار افت عملکرد، کاهش انگیزه و تمایل به ترک سازمان می‌شوند.

بررسی‌های اولیه نشان داده است که مشکل صرفاً به مهارت فنی یا سطح حقوق محدود نمی‌شود؛ بلکه در بسیاری از موارد، عدم تناسب میان ویژگی‌های شخصیتی کارکنان، فرهنگ سازمانی، نوع دپارتمان و سبک مدیریتی سرپرستان نقش مهمی در این مسئله ایفا می‌کند.

در این پروژه به‌عنوان یک Data Scientist، مأموریت شما توسعه مدلی است که بتواند میزان انطباق هر کارمند با محیط سازمان را پیش‌بینی کرده و به تیم منابع انسانی در تصمیم‌گیری‌های مرتبط با جذب، نگهداشت و جابه‌جایی داخلی نیروها کمک کند.

---

## 📊 درباره دیتاست

این دیتاست شامل اطلاعات **10,000 کارمند** و **12 ویژگی** مرتبط با شخصیت، ترجیحات کاری و شرایط سازمانی است.

### Dataset Information

```text
➤ Rows             10,000
➤ Columns              12
```

### Features

| Column                      | Description                         |
| --------------------------- | ----------------------------------- |
| employee_id                 | شناسه یکتای کارمند                  |
| department                  | دپارتمان محل فعالیت                 |
| manager_leadership_style    | سبک رهبری مدیر مستقیم               |
| pers_openness               | میزان پذیرش تجربه‌های جدید          |
| pers_conscientiousness      | وظیفه‌شناسی                         |
| pers_extraversion           | برون‌گرایی                          |
| pers_agreeableness          | توافق‌پذیری                         |
| pers_neuroticism            | روان‌رنجوری                         |
| work_flexibility_preference | ترجیح فرد نسبت به انعطاف‌پذیری کاری |
| years_at_company            | سابقه حضور در شرکت                  |
| p_o_fit_score               | امتیاز انطباق فرد با سازمان         |
| fit_eligibility_class       | سطح نهایی انطباق (متغیر هدف)        |

---

## 🧠 منطق طراحی داده‌ها (Synthetic Yet Realistic Data)

داده‌های این پروژه به‌صورت سنتتیک (Synthetic) تولید شده‌اند، اما ساختار آن‌ها بر اساس مفاهیم واقعی روان‌شناسی سازمانی و رفتار سازمانی طراحی شده است.

در فرآیند تولید داده‌ها، روابط منطقی و الگوهای رفتاری واقعی در نظر گرفته شده‌اند تا محیطی نزدیک به شرایط واقعی سازمان‌ها شبیه‌سازی شود.

### نمونه‌ای از قواعد شبیه‌سازی

* کارکنان دارای **برون‌گرایی بالا** معمولاً در واحدهای فروش و ارتباط با مشتری عملکرد بهتری دارند.
* افراد دارای **پذیرش تجربه‌های جدید (Openness) بالا** با سبک‌های مدیریتی انعطاف‌پذیر سازگاری بیشتری نشان می‌دهند.
* سبک‌های مدیریتی کنترل‌گر (Micromanagement) می‌توانند امتیاز انطباق افراد خلاق و مستقل را کاهش دهند.
* سابقه حضور در سازمان و ترجیحات کاری افراد نیز در محاسبه امتیاز نهایی انطباق نقش دارند.

---

## 
---

## 🛠️ ابزارها و فناوری‌ها

| بخش            | فناوری              |
| -------------- | ------------------- |
| تحلیل داده     | Pandas, NumPy       |
| مصورسازی داده  | Matplotlib, Seaborn |
| یادگیری ماشین  | Scikit-Learn        |
| ذخیره مدل      | Joblib              |
| داشبورد تعاملی | Streamlit           |
| محیط توسعه     | Jupyter Notebook    |

---

## 📄 گزارش تحلیلی
* تحلیل قدم به قدم و پیشنهادات علمی و عملی 

---

## 🎓 هدف پروژه

این پروژه با هدف توسعه مهارت‌های عملی در حوزه‌های زیر طراحی شده است:

* Data Analysis
* Organizational Analytics
* Human Resources Analytics (HR Analytics)
* Machine Learning
* Predictive Modeling
* Dashboard Development

این پروژه نمونه‌ای از کاربرد علم داده در حل مسائل واقعی منابع انسانی و بهبود تصمیم‌گیری‌های سازمانی مبتنی بر داده است.

# 🧠 Person–Organization Fit Predictor

This project was developed to evaluate and predict how well employees align with an organization's culture, work environment, and managerial structure. By combining concepts from **Organizational Psychology, Data Analytics, and Machine Learning**, the project aims to measure the level of **Person–Organization (P–O) Fit** for employees.

The primary objective is to support Human Resources (HR) teams in identifying employees who may struggle to adapt to their current work environment, experience job dissatisfaction, or become at risk of leaving the organization.

---

## 🏢 Business Scenario

The technology company **SynapseTech** has recently faced a hidden organizational challenge. Despite offering competitive salaries and attractive benefits, some employees experience declining performance, reduced engagement, and increased turnover intentions after joining the company.

Initial investigations revealed that the problem is not solely related to technical skills or compensation. In many cases, a mismatch between employees' personality traits, organizational culture, departmental environment, and leadership styles plays a significant role.

As a Data Scientist, your mission is to develop a predictive model capable of estimating each employee's level of organizational fit and providing valuable insights to HR teams for recruitment, retention, and internal mobility decisions.

---

## 📊 Dataset Overview

The dataset contains information about **10,000 employees** and **12 features** related to personality traits, workplace preferences, and organizational characteristics.

### Dataset Information

```text
➤ Rows             10,000
➤ Columns              12
```

### Features

| Column                      | Description                                               |
| --------------------------- | --------------------------------------------------------- |
| employee_id                 | Unique employee identifier                                |
| department                  | Employee department                                       |
| manager_leadership_style    | Leadership style of the direct manager                    |
| pers_openness               | Openness to experience score                              |
| pers_conscientiousness      | Conscientiousness score                                   |
| pers_extraversion           | Extraversion score                                        |
| pers_agreeableness          | Agreeableness score                                       |
| pers_neuroticism            | Neuroticism score                                         |
| work_flexibility_preference | Preference for workplace flexibility                      |
| years_at_company            | Employee tenure within the company                        |
| p_o_fit_score               | Person–Organization Fit score                             |
| fit_eligibility_class       | Final organizational fit classification (Target Variable) |

---

## 🧠 Synthetic Yet Realistic Data Design

Although the dataset is synthetically generated, its structure is based on well-established principles from **Organizational Psychology**, **Behavioral Science**, and **Human Resource Management**.

The data generation process incorporates realistic relationships and behavioral patterns commonly observed in modern organizations, creating a simulation environment that closely resembles real-world workplace dynamics.

### Examples of Embedded Business Rules

* Employees with **high extraversion** tend to perform better in sales and customer-facing roles.
* Individuals with **high openness to experience** generally adapt more effectively to flexible and innovative leadership styles.
* Highly controlling management approaches (**Micromanagement**) may reduce the organizational fit of creative and independent employees.
* Employee tenure and workplace flexibility preferences also influence overall organizational fit scores.

---

## 🛠️ Technologies & Tools

| Category                | Technologies        |
| ----------------------- | ------------------- |
| Data Analysis           | Pandas, NumPy       |
| Data Visualization      | Matplotlib, Seaborn |
| Machine Learning        | Scikit-Learn        |
| Model Persistence       | Joblib              |
| Interactive Dashboard   | Streamlit           |
| Development Environment | Jupyter Notebook    |

---

## 📄 Analytical Report

 * Detailed Step-by-Step Analysis and Evidence-Based Practical Suggestions
---

## 🎓 Project Purpose

This project was developed to strengthen practical skills in:

* Data Analysis
* Organizational Analytics
* Human Resources Analytics (HR Analytics)
* Machine Learning
* Predictive Modeling
* Dashboard Development

It demonstrates how Data Science can be applied to solve real-world HR challenges and support data-driven organizational decision-making.
