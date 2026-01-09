# Berg’s AI Ordering System

**AI-powered ordering interface for Berg’s Ice Cream Shop**

[![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.30+-red.svg)](https://streamlit.io/)
[![OpenAI](https://img.shields.io/badge/OpenAI-GPT--4o--mini-green.svg)](https://openai.com/)

> A proof-of-concept conversational AI system that bridges natural language customer queries with structured menu data, demonstrating practical AI application in small business operations.

-----

## 🎯 Project Overview

Berg’s AI Ordering System is a working demo built for my father-in-law’s ice cream shop. The application combines traditional menu browsing with intelligent Q&A and smart recommendations to provide customers with an intuitive ordering experience.

**Key Innovation:** Hybrid rule-based + LLM approach that handles 80% of queries instantly (no API cost) while leveraging OpenAI for complex conversational interactions.

### What Makes This Different

- **Real Business Application:** Built for actual deployment (demo approved by store manager)
- **Cost-Optimized AI:** Rule-based system handles common queries; LLM only for complex cases
- **Graceful Degradation:** System remains fully functional if OpenAI API is unavailable
- **Dietary Intelligence:** Automatic filtering for vegan, gluten-free, and allergen concerns
- **Smart Recommendations:** Contextual topping suggestions based on flavor selection

-----

## 🚀 Features

### 1. Intelligent Q&A System

- Natural language menu queries
- Instant dietary restriction filtering (vegan, gluten-free)
- Conversational context with full chat history
- Sub-100ms response time for common queries

### 2. Interactive Order Builder

- Guided step-by-step ordering process
- Real-time price calculation
- Smart topping recommendations based on flavor
- Quantity selection and order customization

### 3. Menu Search & Filter

- Keyword-based search across all menu items
- Filter by type (flavors, cones, toppings)
- Filter by dietary requirements
- Formatted results table with pricing

### 4. Shopping Cart & Checkout

- Session-based cart management
- Order history with timestamps
- Customer information capture
- Pickup/delivery selection
- Order total calculation

-----

## 🛠️ Tech Stack

|Component |Technology |Purpose |
|----------------------|-----------------------|-------------------------------------|
|**Frontend** |Streamlit |Rapid UI prototyping with Python |
|**Data Layer** |Pandas |Efficient menu filtering and querying|
|**AI Engine** |OpenAI GPT-4o-mini |Natural language understanding |
|**Session Management**|Streamlit Session State|Cart and conversation persistence |
|**Language** |Python 3.11+ |Core application logic |

-----

## 📁 Project Structure

```
bergs-ai-ordering/
├── app.py # Main application
├── requirements.txt # Python dependencies
├── .venv/ # Virtual environment
├── README.md # This file
├── ARCHITECTURE.md # Technical deep-dive
└── PORTFOLIO.md # Development story (coming soon)
```

-----

## 🏃‍♂️ Quick Start

### Prerequisites

- Python 3.11 or higher
- OpenAI API key (optional - system works without it)
- Git

### Installation

1. **Clone the repository**

```bash
git clone https://github.com/geegorbee/bergs-ai-ordering.git
cd bergs-ai-ordering
```
1. **Create virtual environment**

```bash
python -m venv .venv

# Windows
.venv\Scripts\activate.bat

# Linux/Mac
source .venv/bin/activate
```
1. **Install dependencies**

```bash
pip install -r requirements.txt
```
1. **Set up OpenAI API key** (optional)

```bash
# Windows
set OPENAI_API_KEY=your_key_here

# Linux/Mac
export OPENAI_API_KEY=your_key_here
```

**Note:** System works without API key using rule-based responses only.
1. **Run the application**

```bash
streamlit run app.py
```
1. **Open in browser**
- Streamlit will automatically open `http://localhost:8501`
- If not, manually navigate to the URL shown in terminal

-----

## 💡 Usage Examples

### Example 1: Dietary Query

```
User: "Show me vegan options"
System: [Filters menu] → Displays: Mango Sorbet, Strawberry Sorbet
```

### Example 2: Conversational Q&A

```
User: "What goes well with chocolate ice cream?"
AI Assistant: "Great choice! Hot Fudge and Sprinkles are classic pairings
with chocolate. For something unique, try Crushed Oreos!"
```

### Example 3: Complete Order

```
1. Select Flavor: Chocolate ($3.75)
2. Select Cone: Waffle Cone ($1.25)
3. Add Toppings: Hot Fudge ($0.75), Sprinkles ($0.50)
4. Set Quantity: 2
5. Enter Name: "John"
6. Choose: "Pickup"
→ Total: $12.50
→ Added to cart!
```

-----

## 🎨 Screenshots

### Main Interface

*Coming soon - Demo screenshots showing Q&A, order builder, and cart*

### Chat Interaction

*Coming soon - Example conversation with AI assistant*

### Order Flow

*Coming soon - Step-by-step order creation process*

-----

## 🏗️ Architecture Highlights

### Hybrid Intelligence System

```
User Query
↓
Rule-Based Engine (Fast, Free)
├─ Match? → Instant Response
└─ No Match? → LLM Engine (Smart, Accurate)
```

**Why This Approach?**

- **Performance:** 80% of queries answered in <10ms
- **Cost:** Only pay for complex queries ($0.10/month in testing)
- **Reliability:** System works even if OpenAI API is down

### Data Flow

```
Menu (Pandas DataFrame)
↓
Filter Engine → [vegan=True, gluten_free=True, type="flavor"]
↓
Results → Streamlit UI
↓
User Selection → Session State → Cart
```

For detailed technical documentation, see <ARCHITECTURE.md>.

-----

## 🔒 Security Considerations

### Current (Demo) State

- ✅ OpenAI API key via environment variable
- ✅ No sensitive data storage
- ✅ Session isolation (per-user)
- ⚠️ No authentication (open access)
- ⚠️ No input sanitization (demo only)

### Production Requirements

- 🔐 Secret management service (AWS Secrets Manager)
- 🔐 Input validation and sanitization
- 🔐 HTTPS enforcement
- 🔐 Role-based access control (staff vs. customer)
- 🔐 PCI DSS compliance for payment processing

-----

## 📊 Performance Metrics

|Operation |Current Performance|Target (Production)|
|----------------|-------------------|-------------------|
|Rule-based query|<10ms |<10ms |
|LLM query |1-3 seconds |<500ms (cached) |
|Menu filter |<50ms |<50ms |
|Order submission|<100ms |<100ms |

**Optimization Opportunities:**

- Implement response caching (Redis)
- Async LLM calls with loading states
- Database indexing (when migrating from Pandas)

-----

## 🚦 Current Status

**Phase:** ✅ Working Demo / Proof of Concept

**Completed:**

- ✅ Core ordering functionality
- ✅ Rule-based Q&A system
- ✅ LLM integration with fallback
- ✅ Smart recommendations
- ✅ Cart management
- ✅ Dietary filtering
- ✅ Real-world demo to store manager (positive feedback)

**In Progress:**

- 🔄 Documentation (Architecture ✅, Portfolio 📝)
- 🔄 Web deployment (Streamlit Cloud planned)

**Planned:**

- 📋 SMS/Email order notifications (Twilio)
- 📋 Voice interface (Web Speech API)
- 📋 Order history database (SQLite → PostgreSQL)
- 📋 Admin dashboard for menu management
- 📋 Real-time inventory tracking
- 📋 MCP integration for advanced AI orchestration

-----

## 🎯 Roadmap

### Short-Term (Next 2 Months)

1. Deploy to Streamlit Cloud or Heroku
1. Add order persistence (SQLite)
1. Implement SMS notifications
1. Add allergy warnings and ingredient details

### Medium-Term (3-6 Months)

1. Voice ordering interface
1. Dynamic pricing/specials system
1. Ingredient inventory tracking
1. Analytics dashboard

### Long-Term (6-12 Months)

1. Model Context Protocol (MCP) integration
1. Customer accounts with preferences
1. Multi-location support
1. Mobile app (React Native)

-----

## 🤝 Contributing

This is a personal portfolio project, but feedback and suggestions are welcome!

**To suggest improvements:**

1. Open an issue describing the enhancement
1. Reference specific use cases or pain points
1. Include technical details if proposing architecture changes

-----

## 📝 Technical Documentation

- **<ARCHITECTURE.md>** - Deep technical dive into system design, data flows, and implementation details
- **<PORTFOLIO.md>** *(coming soon)* - Development journey, challenges, and lessons learned

-----

## 🔧 Troubleshooting

### Issue: Streamlit won’t start

```bash
# Check Python version (requires 3.11+)
python --version

# Verify virtual environment is activated
# Windows: Should see (.venv) in prompt
# Linux/Mac: echo $VIRTUAL_ENV should show path

# Reinstall dependencies
pip install -r requirements.txt --force-reinstall
```

### Issue: “ModuleNotFoundError: No module named ‘streamlit’”

```bash
# Activate virtual environment first
.venv\Scripts\activate.bat # Windows
source .venv/bin/activate # Linux/Mac

# Then install
pip install streamlit
```

### Issue: OpenAI API errors

```bash
# Verify API key is set
echo %OPENAI_API_KEY% # Windows
echo $OPENAI_API_KEY # Linux/Mac

# System will work without API key (rule-based mode only)
# Unset to test fallback behavior
```

### Issue: Deprecation warnings

```python
# Update width parameter if you see container_width warnings
# Old: st.dataframe(df, use_container_width=True)
# New: st.dataframe(df, width="stretch")
```

-----

## 💰 Cost Analysis

### Development Costs

- **Time:** ~40 hours (design, development, testing)
- **OpenAI API:** $0.10/month (testing only)
- **Total:** <$1/month

### Production Estimates (50 orders/day)

|Service |Cost |Notes |
|----------------|--------------|-----------------------|
|Hosting (Heroku)|$7/month |Hobby tier |
|Database |$9/month |Heroku Postgres |
|OpenAI API |$5/month |~30% of queries use LLM|
|Domain + SSL |$15/year |Custom domain |
|**Total** |**~$22/month**|**$0.44/order** |

**ROI:** Average ice cream order: $8-12. AI system adds ~5% operational cost while reducing order errors and improving customer experience.

-----

## 🎓 Skills Demonstrated

This project showcases:

**AI/ML Engineering:**

- LLM prompt engineering and system design
- Hybrid AI architecture (rule-based + neural)
- Cost optimization strategies
- Graceful degradation patterns

**Software Development:**

- Python application architecture
- API integration (OpenAI)
- State management (session handling)
- Data manipulation (Pandas)

**Product Thinking:**

- Real-world business application
- User experience design
- Cost-benefit analysis
- Iterative development

**Security Awareness:**

- Secure API key management
- Input validation considerations
- Data privacy (session isolation)
- Production readiness planning

-----

## 📧 Contact

**Gerald Brown**

- 📧 Email: gerald.brown@alumni.utoronto.ca
- 💼 LinkedIn: [linkedin.com/in/gerald-brown-63168223a](https://linkedin.com/in/gerald-brown-63168223a)
- 🐙 GitHub: [github.com/geegorbee](https://github.com/geegorbee)
- 🎯 TryHackMe: CybrSerp3nt

-----

## 📄 License

This project is part of a personal portfolio. Code is provided for demonstration purposes.

-----

## 🙏 Acknowledgments

- **Berg’s Ice Cream Shop** - Business case and real-world testing
- **Store Manager** - Feedback on demo and feature validation
- **Emma** - Support during development (and patience with delayed deployment)
- **OpenAI** - GPT-4o-mini API for natural language capabilities
- **Streamlit** - Rapid prototyping framework

-----

## 📚 Related Projects

Check out my other cybersecurity and AI projects:

- **[PwC Cybersecurity Virtual Internship](https://github.com/geegorbee/Cybersecurity-Portfolio/tree/main/Virtual-Internships/PwC-Cyber)** - Enterprise risk assessment and SOX compliance
- **[Active Directory Security Series](https://github.com/geegorbee/Cybersecurity-Portfolio/tree/main/TryHackMe/Active-Directory-Series)** - AD fundamentals, hardening, and attack techniques
- **More projects:** [Cybersecurity Portfolio](https://github.com/geegorbee/Cybersecurity-Portfolio)

-----

**Built with ❤️ by Gerald Brown | AI Security Engineer in Training | CBS, NL**

-----

## 🔖 Version History

- **v1.0** (January 2026) - Initial working demo
- Core ordering functionality
- Rule-based + LLM Q&A system
- Smart recommendations
- Cart management
- Streamlit deprecation fixes (use_container_width → width=“stretch”)

-----

*Last Updated: January 8, 2026*
