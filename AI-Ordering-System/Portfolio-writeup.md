# Berg’s AI Ordering System

**An AI-powered ordering interface for a local ice cream shop**

**Status:** Working prototype/demo
**Development Period:** September-October 2025
**Tech Stack:** Python, Streamlit, Pandas, OpenAI API
**GitHub:** [Link to repository when published]

-----

## Overview

Berg’s AI Ordering System is a proof-of-concept web application designed to modernize the ordering experience for Berg’s Ice Cream Shop. The system provides an intuitive interface for customers to browse the menu, receive smart recommendations, and build orders with dietary preferences in mind.

**Problem Solved:** Small businesses often lack resources for custom digital solutions. This project demonstrates how AI-assisted development can create practical business tools quickly and cost-effectively.

-----

## Project Context

### The Business Need

Berg’s Ice Cream Shop, a family-owned business, wanted to explore options for:

- Modernizing their ordering process
- Accommodating dietary restrictions (vegan, gluten-free)
- Providing product recommendations to increase average order value
- Potential for online/remote ordering integration

### Development Approach

Rather than a traditional planned development cycle, this project evolved organically through **AI-assisted rapid prototyping**:

- Identified core features needed for minimal viable product
- Built working prototype using AI pair programming (ChatGPT)
- Iterated based on immediate feedback
- Demonstrated to stakeholders early for validation

**Development Philosophy:** Get something working quickly, validate with stakeholders, then enhance based on real feedback.

-----

## Current Features (Phase 1 - Working Demo)

### ✅ Menu Management System

- **Complete product catalog:** Flavors, cones, and toppings with pricing
- **Dietary information:** Vegan and gluten-free indicators for all items
- **Dynamic filtering:** Search by dietary needs or keywords
- **Clear pricing transparency:** All costs visible upfront

### ✅ Intelligent Search & Q&A

- **Keyword-based search:** Natural language queries (“vegan”, “chocolate”, “toppings”)
- **Menu filtering:** Results displayed in clean, scannable table format
- **Context-aware responses:** Handles questions about dietary options, ingredients, availability

### ✅ Smart Recommendations

- **Flavor-based suggestions:** System recommends complementary toppings based on ice cream flavor selection
- **Business logic:** Hardcoded recommendations ensure consistency and control
- **Upselling potential:** Increases average order value through relevant suggestions

### ✅ Order Builder Interface

- **Step-by-step workflow:**
1. Select flavor from full menu
1. Choose cone type
1. Set quantity (1-20 with validation)
1. Add optional toppings (multi-select)
- **Real-time calculations:** Subtotal updates as selections are made
- **Visual feedback:** Clear indication of current selections

### ✅ Shopping Cart System

- **Session-based storage:** Orders persist during browsing session
- **Multi-item support:** Build multiple orders before finalizing
- **Order summary:** Clear display of all items with individual and total pricing
- **Timestamp tracking:** Each order logged with date/time for record-keeping

### ✅ Order Finalization

- **Customer information:** Name collection for order association
- **Fulfillment options:** Pickup or delivery selection
- **Special instructions:** Notes field for allergies, preferences, timing, etc.

-----

## Technical Architecture

### Core Technologies

**Frontend Framework:**

- **Streamlit** - Rapid web application development
- Clean, responsive interface without custom HTML/CSS/JavaScript
- Built-in session state management for cart functionality

**Data Management:**

- **Pandas** - Menu data handling and filtering
- Structured DataFrames for product catalog
- Efficient querying for search functionality

**Development Environment:**

- **Python 3.8+** - Core programming language
- **Virtual environment (.venv)** - Isolated dependency management
- **pip** - Package management

**Planned Integration (Phase 2):**

- **OpenAI API** - Natural language understanding for conversational ordering
- Currently uses keyword matching; API integration prepared for future enhancement

### Application Flow

```
User Input (search/question)
↓
Keyword Matching & Filtering
↓
Display Results (menu items)
↓
Order Building (flavor + cone + toppings + quantity)
↓
Recommendation Engine (suggest toppings based on flavor)
↓
Add to Cart (session state storage)
↓
Order Summary (review all items + total)
↓
Finalization (customer info + pickup/delivery + notes)
↓
[Future: Integration with POS/email system]
```

### Key Technical Features

**Session State Management:**

- Cart persists across page interactions
- Multiple orders tracked simultaneously
- State cleared only on session end or explicit reset

**Data Filtering Logic:**

```python
# Dietary filter example
if "vegan" in query:
filtered_menu = menu[menu["vegan"] == True]
if "gluten" in query:
filtered_menu = menu[menu["gluten_free"] == True]
```

**Smart Recommendations:**

```python
# Flavor-based topping suggestions
if "chocolate" in selected_flavor:
recommendations = ["Hot Fudge", "Sprinkles"]
if "vanilla" in selected_flavor:
recommendations = ["Hot Fudge", "Crushed Oreos"]
```

**Price Calculation:**

```python
# Real-time order total
subtotal = qty * (price_of(flavor) + price_of(cone) + sum(price_of(t) for t in toppings))
```

-----

## Development Journey

### Phase 1: Prototype (Completed ✅)

**Goal:** Prove the concept works with core functionality

**Achievements:**

- Working menu system with filtering
- Order builder with cart functionality
- Smart topping recommendations
- Clean, intuitive interface
- Successfully demonstrated to store manager

**Timeline:** ~2-3 weeks of iterative development

**Challenges Encountered:**

1. **Cross-platform deployment:** Initial difficulties running on Chromebook
- *Solution:* Focused on local demo first; cloud deployment planned for Phase 2
1. **Streamlit deprecation warnings:** API changes in framework
- *Solution:* Updated `use_container_width` → `width` parameter (fixed Jan 8, 2026)
1. **Balancing features vs. simplicity:** Wanted to add everything immediately
- *Solution:* Focused on MVP; documented enhancement roadmap for future

**Stakeholder Feedback:**

- Store manager enthusiastic about concept
- Appreciated clean, simple interface
- Requested ideas incorporated into Phase 2 roadmap

-----

### Phase 2: AI Enhancement (Planned)

**Goal:** Add natural language understanding and conversational interface

**Planned Features:**

- Full OpenAI API integration for natural language order taking
- Conversational interface (“I’d like a large chocolate cone with sprinkles”)
- Context-aware follow-up questions
- Dynamic recommendation engine based on order history
- Seasonal menu updates via AI-generated descriptions

**Technical Approach:**

- Integrate OpenAI Chat Completions API
- System prompt tuned for ice cream shop context
- User input → GPT processing → Structured order data
- Maintain existing keyword fallback for reliability

-----

### Phase 3: Production Deployment (Future)

**Goal:** Full business integration for customer-facing use

**Deployment Options Explored:**

**Option A: In-Store Kiosk**

- Tablet/laptop interface at counter
- Staff-assisted ordering
- Immediate order capture

**Option B: Website Integration**

- Embed into existing Berg’s website
- Online ordering with pickup/delivery
- Email integration for order notification

**Option C: Hybrid System**

- Both in-store and online availability
- Unified order management system
- Integration with existing workflow

**Additional Enhancements:**

- **POS Integration:** Direct order submission to existing system
- **Inventory Tracking:** Real-time availability updates
- **Automated Reordering:** Low stock alerts and supplier integration
- **Number Ticket System:** Queue management for busy periods
- **Voice Interface:** Hands-free ordering for accessibility
- **MCP Integration:** Multi-model AI orchestration for complex workflows

-----

## Skills Demonstrated

### Software Development

✅ **Python Programming** - Application logic, data handling, function design
✅ **Web Framework (Streamlit)** - Rapid UI development
✅ **API Integration** - OpenAI setup (prepared for Phase 2)
✅ **Version Control** - Git/GitHub for code management
✅ **Virtual Environments** - Dependency isolation and management

### Business & Product Thinking

✅ **Stakeholder Engagement** - Requirements gathering from business owner
✅ **User Experience Design** - Intuitive workflow for non-technical users
✅ **Agile Development** - Iterative prototyping with feedback loops
✅ **Scalability Planning** - Roadmap from demo → deployment → integration
✅ **Problem Solving** - Technical constraints (platform compatibility)

### AI/Machine Learning

✅ **AI-Assisted Development** - Leveraging ChatGPT for rapid prototyping
✅ **API Preparation** - OpenAI integration readiness
✅ **Prompt Engineering** - Planning conversational AI interactions
✅ **Business AI Applications** - Practical LLM use cases beyond chatbots

### Real-World Project Management

✅ **Resource Constraints** - Working with limited time and tools
✅ **Priority Management** - MVP first, enhancements later
✅ **Blockers & Pivots** - Adapting when life events (Emma’s health) intervened
✅ **End-to-End Ownership** - Concept → development → demo → roadmap

-----

## Why This Project Matters

### For Cybersecurity Career:

**1. Demonstrates AI Security Understanding**

- Practical experience with LLM APIs and AI systems
- Understanding of AI-powered application architecture
- Awareness of security considerations in AI deployment (input validation, prompt injection risks)

**2. Shows Development Capabilities**

- Not just theory - built working software
- Full-stack thinking: frontend, backend, data, future integrations
- Security mindset: session management, data handling, user input validation

**3. Business Context Awareness**

- Security isn’t just technical - it’s about enabling business value
- Understanding of business processes, workflow integration, stakeholder needs
- Risk assessment: prototype vs. production, trade-offs, deployment considerations

**4. Forward-Thinking Technical Strategy**

- MCP integration planning (ahead of mainstream adoption)
- Multi-phase development roadmap
- Scalability and integration architecture

### Relevance to Target Roles:

**AI Security Engineer:**

- Direct experience building AI-powered systems
- Understanding of LLM integration points and security implications
- Practical knowledge of AI application development lifecycle

**Security Analyst/SOC Analyst:**

- Application security awareness (session management, input validation)
- Understanding of web application architecture and attack surfaces
- Experience with API integration and third-party service dependencies

**GRC/Compliance:**

- Privacy considerations (customer data handling, PII in orders)
- Business process risk assessment
- Security controls in software development

-----

## Current Status & Next Steps

### ✅ Demo Ready

- Working prototype that can be run locally
- Successfully demonstrated to stakeholders
- Code clean and maintainable
- Documentation (Quick Start Guide) available

### 📋 Immediate Next Steps

1. **Create architecture documentation** - Technical deep-dive on how it works
1. **Publish to GitHub** - Make portfolio-ready with README, docs, code comments
1. **Security review** - Assess potential vulnerabilities before any production consideration
1. **Performance testing** - Load testing, response times, user experience validation

### 🚀 Phase 2 Development (When Time Allows)

1. **OpenAI API integration** - Full natural language ordering
1. **Enhanced UI/UX** - Visual improvements, mobile responsiveness
1. **Testing framework** - Unit tests, integration tests
1. **Deployment planning** - Cloud hosting options, CI/CD pipeline

### 🏢 Business Integration (Future Consideration)

1. **POS integration research** - Technical requirements for Berg’s existing systems
1. **Security hardening** - Production-grade authentication, data encryption, compliance
1. **Stakeholder alignment** - Business case, ROI analysis, deployment timeline
1. **Pilot deployment** - Limited rollout with monitoring and feedback collection

-----

## Lessons Learned

### What Worked Well:

- **AI-assisted development** drastically reduced development time
- **Early stakeholder demo** provided valuable validation and enthusiasm
- **Simple MVP approach** prevented feature creep and scope expansion
- **Iterative methodology** allowed quick pivots based on feedback

### What I’d Do Differently:

- **Document as you go** - Architecture decisions were made organically but not captured in real-time
- **Plan deployment earlier** - Platform compatibility challenges could have been anticipated
- **Set clearer milestones** - Project scope evolved without formal checkpoints
- **Security from the start** - Would incorporate security review earlier in development

### Key Takeaway:

**Rapid prototyping with AI assistance is powerful, but production deployment requires careful planning, security review, and stakeholder alignment.** The technical build is only one piece - business integration, security hardening, and change management are equally critical.

-----

## Portfolio Value

This project demonstrates:

✅ **End-to-end project ownership** - Concept to working demo
✅ **Real-world application** - Actual business need, not just academic exercise
✅ **AI/LLM experience** - Practical AI integration (planned and prepared)
✅ **Full-stack thinking** - Frontend, backend, data, deployment considerations
✅ **Business acumen** - Understanding stakeholder needs, ROI, integration challenges
✅ **Security mindset** - Awareness of risks, data handling, input validation
✅ **Adaptability** - Pivoting when constraints arise (platform issues, time limitations)
✅ **Communication** - Stakeholder demos, documentation, project storytelling

**This is not a tutorial follow-along - this is original development work solving a real problem.**

-----

## Technical Documentation

**Setup Guide:** [Quick Start Guide - separate document]
**Architecture Overview:** [To be created]
**Code Repository:** [GitHub link when published]
**Enhancement Roadmap:** [Detailed in Phase 2/3 sections above]

-----

## Connect

For questions about this project or collaboration opportunities:

📧 gerald.brown@alumni.utoronto.ca
💼 [LinkedIn](https://linkedin.com/in/gerald-brown-63168223a)
🔗 [Full Portfolio](https://github.com/geegorbee/Cybersecurity-Portfolio)

-----

**Project Status:** Active development paused (family priorities); ready to resume
**Demo Availability:** Can be run locally anytime (see Quick Start Guide)
**Code Quality:** Clean, maintainable, documented
**Business Interest:** Stakeholders supportive of future deployment
