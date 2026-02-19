\# 🍽 Hotel New Guru Deo Basera — Restaurant FAQ Bot



A smart FAQ chatbot for \*\*Hotel New Guru Deo Basera\*\* built with \*\*Flask\*\* and \*\*Groq AI (LLaMA 3.3)\*\*. Customers can ask questions about the menu, dietary options, opening hours, reservations, and more — and get instant, helpful answers.



---



\## 🌐 Live Demo

👉 https://restaurant-faq-bot.onrender.com



---



\## 📸 Screenshots



\### FAQ Page

\- Accordion-style FAQ sections

\- Category filters (Menu, Dietary, Hours, Booking, Payment)

\- Live AI chat at the bottom



---



\## ✨ Features



\- ✅ FAQ accordion with category filters

\- ✅ AI-powered chat using Groq API (LLaMA 3.3)

\- ✅ Full menu with prices in Indian Rupees (₹)

\- ✅ Dietary filters (Vegetarian, Vegan, Gluten-Free, Dairy-Free)

\- ✅ Multi-turn conversation memory

\- ✅ Typing animation

\- ✅ Mobile responsive

\- ✅ API key secured via environment variables



---



\## 🛠 Tech Stack



| Technology | Purpose |

|---|---|

| Python 3.x | Backend language |

| Flask | Web framework |

| Groq API | AI responses (LLaMA 3.3 70B) |

| HTML/CSS/JS | Frontend |

| Gunicorn | Production server |

| Render | Free deployment |



---



\## 📁 Project Structure



```

Restaurant-FAQ-Bot/

├── app.py                  ← Flask backend

├── requirements.txt        ← Python dependencies

├── render.yaml             ← Render deployment config

├── .gitignore              ← Files to ignore in Git

├── templates/

│   └── index.html          ← Frontend UI

└── README.md               ← Project documentation

```



---



\## 🚀 Getting Started Locally



\### 1. Clone the repository

```bash

git clone https://github.com/priyanshugupta825/Restaurant-FAQ-Bot.git

cd Restaurant-FAQ-Bot

```



\### 2. Create virtual environment

```bash

python -m venv .venv

```



\### 3. Activate virtual environment



\*\*Windows:\*\*

```bash

.venv\\Scripts\\Activate.ps1

```



\*\*Mac/Linux:\*\*

```bash

source .venv/bin/activate

```



\### 4. Install dependencies

```bash

pip install -r requirements.txt

```



\### 5. Set your Groq API key



\*\*Windows PowerShell:\*\*

```bash

$env:GROQ\_API\_KEY="your-groq-api-key-here"

```



\*\*Mac/Linux:\*\*

```bash

export GROQ\_API\_KEY="your-groq-api-key-here"

```



\### 6. Run the app

```bash

python app.py

```



\### 7. Open in browser

```

http://localhost:5000

```



---



\## 🔑 Getting a Free Groq API Key



1\. Go to 👉 https://console.groq.com

2\. Sign up for free (no credit card needed)

3\. Click \*\*"API Keys"\*\* → \*\*"Create API Key"\*\*

4\. Copy the key (starts with `gsk\_...`)



---



\## 🌍 Deployment on Render (Free)



\### 1. Push code to GitHub

```bash

git add .

git commit -m "deploy"

git push

```



\### 2. Go to Render

1\. Visit 👉 https://render.com

2\. Sign up with GitHub

3\. Click \*\*"New"\*\* → \*\*"Web Service"\*\*

4\. Connect your \*\*Restaurant-FAQ-Bot\*\* repository



\### 3. Fill in settings

| Setting | Value |

|---|---|

| Name | restaurant-faq-bot |

| Region | Singapore (closest to India) |

| Branch | main |

| Runtime | Python |

| Build Command | `pip install -r requirements.txt` |

| Start Command | `gunicorn app:app` |

| Plan | Free |



\### 4. Add Environment Variable

| Key | Value |

|---|---|

| GROQ\_API\_KEY | your-groq-api-key |



\### 5. Click "Create Web Service"

Wait 2-3 minutes — your app will be live at:

```

https://restaurant-faq-bot.onrender.com

```



---



\## 🍽 Menu (Prices in ₹)



\### Starters

| Item | Dietary | Price |

|---|---|---|

| Tomato Soup | V, GF | ₹120 |

| Garlic Bread | V | ₹80 |

| Chicken Wings | GF | ₹220 |

| Bruschetta | V | ₹150 |



\### Mains

| Item | Dietary | Price |

|---|---|---|

| Grilled Salmon | GF, DF | ₹480 |

| Margherita Pizza | V | ₹300 |

| Mushroom Risotto | V, GF | ₹320 |

| Grilled Chicken | GF, DF | ₹380 |

| Vegan Pasta | VG, DF | ₹280 |



\### Desserts

| Item | Dietary | Price |

|---|---|---|

| Chocolate Lava Cake | V | ₹180 |

| Fruit Sorbet | VG, GF, DF | ₹130 |

| Cheesecake | V | ₹160 |



\### Drinks

| Item | Price |

|---|---|

| Fresh Juices | ₹80 |

| Soft Drinks | ₹60 |

| Coffee/Tea | ₹60 |



\*\*Dietary Codes:\*\* V = Vegetarian | VG = Vegan | GF = Gluten-Free | DF = Dairy-Free



---



\## ❓ FAQ Categories



\- 📋 \*\*Menu\*\* — Full menu, popular dishes, prices

\- 🥗 \*\*Dietary\*\* — Vegetarian, Vegan, Gluten-Free, Dairy-Free options

\- 🕐 \*\*Hours\*\* — Opening and closing times

\- 📞 \*\*Booking\*\* — Reservations, location, parking

\- 💳 \*\*Payment\*\* — Accepted payment methods



---



\## ⚠️ Security



\- API key is stored as an \*\*environment variable\*\*

\- Never hardcoded in the source code

\- `.venv/` and `.env` are excluded via `.gitignore`



---



\## 📞 Restaurant Info



\- 📍 \*\*Address:\*\* 123 Main Street, Downtown

\- 📞 \*\*Phone:\*\* (555) 123-4567

\- 📧 \*\*Email:\*\* reservations@hotelgurudebasera.com

\- 🌐 \*\*Website:\*\* www.hotelgurudebasera.com

\- 🚗 \*\*Parking:\*\* Free parking behind restaurant

\- 💳 \*\*Payment:\*\* Cash, Card, UPI accepted



---



\## 👨‍💻 Author



\*\*Priyansh Gupta\*\*

\- GitHub: \[@priyanshugupta825](https://github.com/priyanshugupta825)



---



\## 📄 License



This project is open source and available under the \[MIT License](LICENSE).

