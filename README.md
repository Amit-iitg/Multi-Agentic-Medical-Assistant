# 🩺 AI Medical Assistant# 🩺 AI Medical Assistant



An AI-powered medical assistant that provides healthcare information through text chat and medical image analysis using multiple specialized AI agents.An AI-powered medical assistant that provides healthcare information through text chat and medical image analysis using multiple specialized AI agents.



## 📋 Project Overview## 📋 Project Overview



This application allows users to:This application allows users to:

- Ask medical questions via text chat- Ask medical questions via text chat

- Upload medical images for AI analysis- Upload medical images for AI analysis

- Get responses from specialized AI agents (RAG, Web Search, Image Analysis)- Get responses from specialized AI agents (RAG, Web Search, Image Analysis)

- Access medical literature and real-time health information- Access medical literature and real-time health information



## 📁 Project Structure## 📁 Project Structure



``````

Medical-Assistant/Medical-Assistant/

├── backend/                    # Python FastAPI Server├── backend/                    # Python FastAPI Server

│   ├── main.py                # FastAPI application entry│   ├── main.py                # FastAPI application entry

│   ├── requirements.txt       # Python dependencies│   ├── requirements.txt       # Python dependencies

│   ││   │

│   └── agents/               # AI Agent System│   └── agents/               # AI Agent System

│       ├── agent_decision.py     # LangGraph orchestration│       ├── agent_decision.py     # LangGraph orchestration

│       ├── guardrails.py         # Content safety│       ├── guardrails.py         # Content safety

│       ├── medical_chat_agent.py # General medical chat│       ├── medical_chat_agent.py # General medical chat

│       ││       │

│       ├── rag_agent/            # Document search│       ├── rag_agent/            # Document search

│       │   ├── document_retriever.py│       │   ├── document_retriever.py

│       │   ├── medical_pdfs/     # Medical documents│       │   ├── medical_pdfs/     # Medical documents

│       │   └── rag_db/          # ChromaDB storage│       │   └── rag_db/          # ChromaDB storage

│       ││       │

│       ├── vision_agents/        # Image analysis│       ├── vision_agents/        # Image analysis

│       │   └── image_analysis_agent.py│       │   └── image_analysis_agent.py

│       ││       │

│       └── web_search/           # Real-time search│       └── web_search/           # Real-time search

│           └── web_search_agent.py│           └── web_search_agent.py

││

└── frontend/                   # React Application└── frontend/                   # React Application

    ├── package.json           # Node.js dependencies    ├── package.json           # Node.js dependencies

    ├── src/    ├── src/

    │   ├── App.js    │   ├── App.js

    │   ├── components/    │   ├── components/

    │   │   ├── ChatContainer.js    │   │   ├── ChatContainer.js

    │   │   ├── ChatMessage.js    │   │   ├── ChatMessage.js

    │   │   └── ChatInput.js    │   │   └── ChatInput.js

    │   └── context/    │   └── context/

    │       └── ChatContext.js    │       └── ChatContext.js

    └── public/    └── public/

``````



## 🛠️ Technology Stack## 🛠️ Technology Stack



### Frontend### Frontend

- **React 19.2** - Frontend framework- **React 19.2** - Frontend framework

- **Styled Components** - CSS-in-JS styling- **Styled Components** - CSS-in-JS styling

- **React Markdown** - Markdown rendering- **React Markdown** - Markdown rendering

- **React Dropzone** - File upload- **React Dropzone** - File upload

- **Axios** - HTTP client- **Axios** - HTTP client



### Backend### Backend

- **FastAPI** - Python web framework- **FastAPI** - Python web framework

- **LangGraph** - Multi-agent orchestration- **LangGraph** - Multi-agent orchestration

- **Groq** - AI model inference- **Groq** - AI model inference

- **ChromaDB** - Vector database- **ChromaDB** - Vector database

- **Tavily** - Web search API- **Tavily** - Web search API



## 🚀 How to Run## 🚀 How to Run



### Prerequisites### Prerequisites

- **Python 3.8+** with pip- **Python 3.8+** with pip

- **Node.js 16+** with npm- **Node.js 16+** with npm



### 1. Clone Repository### 1. Clone Repository

```bash```bash

git clone <repository-url>git clone <repository-url>

cd Medical-Assistantcd Medical-Assistant

``````



### 2. Backend Setup### 2. Backend Setup

```bash```bash

# Create virtual environment# Create virtual environment

python -m venv .venvpython -m venv .venv



# Activate virtual environment# Activate virtual environment

# Windows:# Windows:

.venv\Scripts\activate.venv\Scripts\activate

# macOS/Linux:# macOS/Linux:

source .venv/bin/activatesource .venv/bin/activate



# Install dependencies# Install dependencies

pip install -r requirements.txtpip install -r requirements.txt



# Create .env file in backend folder# Create .env file in backend folder

cd backendcd backend

# Add your API keys to .env:# Add your API keys to .env:

# GROQ_API_KEY=your_groq_api_key# GROQ_API_KEY=your_groq_api_key

# TAVILY_API_KEY=your_tavily_api_key# TAVILY_API_KEY=your_tavily_api_key

# LLM_MODEL_NAME=llama-3.3-70b-versatile# LLM_MODEL_NAME=llama-3.3-70b-versatile



# Start backend# Start backend

uvicorn main:app --reload --host 127.0.0.1 --port 8000uvicorn main:app --reload --host 127.0.0.1 --port 8000

``````



### 3. Frontend Setup### 3. Frontend Setup

```bash```bash

# In new terminal# In new terminal

cd frontendcd frontend



# Install dependencies# Install dependencies

npm installnpm install



# Start frontend# Start frontend

npm startnpm start

``````



### 4. Access Application### 4. Access Application

- **Frontend**: `http://localhost:3000`- **Frontend**: `http://localhost:3000`

- **Backend API**: `http://127.0.0.1:8000`- **Backend API**: `http://127.0.0.1:8000`

- **API Docs**: `http://127.0.0.1:8000/docs`- **API Docs**: `http://127.0.0.1:8000/docs`



### API Keys Required### API Keys Required

- **Groq API**: [https://groq.com](https://groq.com) (for AI models)- **Groq API**: [https://groq.com](https://groq.com) (for AI models)

- **Tavily API**: [https://tavily.com](https://tavily.com) (for web search)- **Tavily API**: [https://tavily.com](https://tavily.com) (for web search)
- **Node.js 16+** with npm
- **Git** for cloning

### 1. Clone the Repository
```bash
git clone <repository-url>
cd Medical-Assistant
```

### 2. Backend Setup

#### Install Python Dependencies
```bash
# Create and activate virtual environment
python -m venv .venv

# Windows
.venv\Scripts\activate

# macOS/Linux
source .venv/bin/activate

# Install packages
pip install -r requirements.txt
```

#### Configure API Keys
Create `backend/.env` file:
```env
GROQ_API_KEY=your_groq_api_key_here
TAVILY_API_KEY=your_tavily_api_key_here
LLM_MODEL_NAME=llama-3.3-70b-versatile
```

**Get API Keys:**
- **Groq API**: [https://groq.com](https://groq.com) (for AI models)
- **Tavily API**: [https://tavily.com](https://tavily.com) (for web search)

### 3. Frontend Setup
```bash
# Navigate to frontend directory
cd frontend

# Install Node.js dependencies
npm install
```

### 4. Start Both Services

#### Terminal 1: Start Backend
```bash
cd backend
uvicorn main:app --reload --host 127.0.0.1 --port 8000
```
✅ Backend running at: `http://127.0.0.1:8000`

#### Terminal 2: Start Frontend
```bash
cd frontend
npm start
```
✅ Frontend running at: `http://localhost:3000`

### 5. Access the Application
1. **Open browser**: Navigate to `http://localhost:3000`
2. **Start chatting**: Ask medical questions or upload images
3. **API docs**: Visit `http://127.0.0.1:8000/docs` for backend documentation

---

## � Project Structure

### **Frontend Stack**
- **React 19.2**: Modern frontend framework with hooks and functional components
- **Styled Components**: CSS-in-JS for component-based styling
- **React Markdown**: Professional markdown rendering with custom components
- **React Dropzone**: Drag-and-drop file upload with visual feedback
- **React Icons**: Comprehensive icon library for UI elements
- **Axios**: HTTP client for API communication

### **Frontend Architecture & Features**
- **ChatGPT-style Interface**: Professional chat layout that transitions from centered input to full conversation
- **Smart Typing Animation**: New messages type character-by-character, existing messages load instantly
- **Image Upload Flow**: Files immediately move from input to chat when sent, no duplicate display
- **Professional Markdown**: Bold headers, proper lists, clean formatting without distracting colors
- **Session Management**: Conversation history persisted in localStorage across browser refreshes
- **Responsive Design**: Optimized for both desktop and mobile viewing

### **Backend Stack**
- **FastAPI**: REST API framework
- **LangGraph**: Agent orchestration and workflow
- **LangChain**: LLM integration and processing
- **ChromaDB**: Vector database for RAG
- **Groq**: LLM inference
- **Tavily**: Web search API

### **Key Dependencies**
```python
# Core Framework
fastapi>=0.104.1
uvicorn[standard]>=0.24.0

# Agent Orchestration
langgraph>=0.0.40
langchain>=0.1.0
langchain-core>=0.1.0

# AI Models & APIs
langchain-groq>=0.0.1
langchain-tavily>=0.0.1
groq>=0.4.1

# Vector Database
chromadb>=0.4.15
sentence-transformers>=2.2.2

# Document Processing
PyPDF2>=3.0.1
transformers>=4.35.0
```

### **Frontend Dependencies (package.json)**
```json
{
  "dependencies": {
    "react": "^19.2.0",
    "react-dom": "^19.2.0",
    "styled-components": "^6.1.19",
    "react-markdown": "^10.1.0",
    "react-dropzone": "^14.3.8",
    "react-icons": "^5.5.0",
    "axios": "^1.13.2",
    "remark-gfm": "^4.0.1",
    "rehype-raw": "^7.0.0"
  }
}
```

### **Configuration Requirements**

Create `.env` file in `backend/` directory:
```env
GROQ_API_KEY=your_groq_api_key_here
TAVILY_API_KEY=your_tavily_api_key_here
LLM_MODEL_NAME=llama-3.3-70b-versatile
```

---

## 🚀 Setup & Running

### **Prerequisites**
- **Python 3.8+** with pip
- **Node.js 16+** with npm 
- **API Keys**: Groq API and Tavily API (see configuration below)

### **1. Clone Repository**
```bash
git clone <your-repository-url>
cd Medical-Assistant
```

### **2. Backend Setup**

#### **Install Python Dependencies**
```bash
# Create virtual environment
python -m venv .venv

# Activate virtual environment
# Windows:
.venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate

# Install all required packages
pip install -r requirements.txt
```

#### **Configure Environment Variables**
```bash
# Navigate to backend directory
cd backend

# Create .env file with your API keys
# Copy the template and add your keys:
```

**Create `backend/.env` file:**
```env
GROQ_API_KEY=your_groq_api_key_here
TAVILY_API_KEY=your_tavily_api_key_here
LLM_MODEL_NAME=llama-3.3-70b-versatile
```

**Get API Keys:**
- **Groq API**: Sign up at [https://groq.com](https://groq.com)
- **Tavily API**: Sign up at [https://tavily.com](https://tavily.com)

#### **Setup Medical Document Database (Optional)**
```bash
# Add medical PDFs to the documents folder
cd agents/rag_agent

# Create directory and add your PDF files
mkdir medical_pdfs
# Copy your medical PDF files to this directory

# Build the vector database
python build_rag_vectorstore.py
```

### **3. Frontend Setup**

#### **Install Node.js Dependencies**
```bash
# Navigate to frontend directory
cd frontend

# Install all React packages
npm install

# All required packages are already in package.json:
# - React 19.2, Styled Components, React Markdown, etc.
```

### **4. Start the Application**

#### **Step 1: Start Backend Server**
```bash
# In one terminal window, navigate to backend
cd backend

# Start FastAPI server
uvicorn main:app --reload --host 127.0.0.1 --port 8000
```
**Backend will be available at:** `http://127.0.0.1:8000`

#### **Step 2: Start Frontend Development Server**
```bash
# In another terminal window, navigate to frontend
cd frontend

# Start React development server
npm start
```
**Frontend will be available at:** `http://localhost:3000`

#### **Step 3: Access the Application**
1. **Open your browser** and go to `http://localhost:3000`
2. **Start chatting** with the AI medical assistant
3. **Upload medical images** using drag-and-drop
4. **View API documentation** at `http://127.0.0.1:8000/docs`

### **5. Verify Setup**

#### **✅ Backend Health Check**
- Visit `http://127.0.0.1:8000/docs` - should show FastAPI documentation
- Check terminal for any error messages
- Ensure `.env` file contains valid API keys

#### **✅ Frontend Health Check**
- Visit `http://localhost:3000` - should show the medical assistant interface
- Check browser console for any JavaScript errors
- Test typing a message and uploading an image

#### **✅ Full Integration Test**
1. **Send a text message**: "What are the symptoms of diabetes?"
2. **Upload a medical image** with drag-and-drop
3. **Verify responses** appear with proper markdown formatting
4. **Check typing animation** works for new messages
5. **Refresh page** and verify conversation history loads instantly

---

## 📊 Request Flow Examples

### **Text Query Example**
```
User: "What are the symptoms of diabetes?"
├─ Guardrails: ✅ Safe medical query
├─ Image Detection: ❌ No image
├─ Agent Routing: LLM selects "RAG_AGENT"
├─ RAG Agent: 
│  ├─ Vector search in medical documents
│  ├─ Retrieve relevant diabetes information
│  └─ Generate contextual response
└─ Response: "Diabetes symptoms include frequent urination, excessive thirst..."
```

### **Image Upload Example**
```
User: Uploads skin lesion image + "What is this?"
├─ Guardrails: ✅ Bypass for medical image
├─ Image Detection: ✅ Route to IMAGE_ANALYSIS_AGENT
├─ Image Agent:
│  ├─ Save temporary image file
│  ├─ AI vision analysis
│  ├─ Medical interpretation
│  └─ Cleanup temporary file
└─ Response: "This appears to be a benign skin condition..."
```

### **Web Search Example**
```
User: "Latest COVID-19 treatment guidelines"
├─ Guardrails: ✅ Safe medical query
├─ Image Detection: ❌ No image
├─ Agent Routing: LLM selects "WEB_SEARCH_PROCESSOR_AGENT"
├─ Web Search Agent:
│  ├─ Tavily API search
│  ├─ Process search results
│  └─ Summarize latest information
└─ Response: "According to recent guidelines from CDC..."
```

---

## 🛡️ Safety & Guardrails

### **Content Safety**
- Pre-processing input validation
- Medical appropriateness checking
- Harmful content filtering

### **Data Privacy**
- Session-based memory (no persistent storage)
- Temporary file cleanup for images
- No personal data logging

### **Error Handling**
- Graceful fallbacks between agents
- Comprehensive exception handling
- User-friendly error messages

---

## 🔧 Customization & Extension

### **Adding New Agents**
1. Create agent file in `agents/` directory
2. Add to routing logic in `agent_decision.py`
3. Update frontend agent list

### **Modifying RAG Database**
1. Add PDFs to `agents/rag_agent/medical_pdfs/`
2. Run `build_rag_vectorstore.py`
3. Vector database automatically updates

### **Changing LLM Models**
Update `.env` file:
```env
LLM_MODEL_NAME=your_preferred_model
GROQ_API_KEY=your_api_key
```

---

## 📝 API Documentation

### **Endpoints**

#### **POST /chat**
Text-only medical queries
```json
{
  "message": "What causes headaches?",
  "session_id": "unique_session_id"
}
```

#### **POST /upload**
Image upload with optional text
```json
{
  "file": "medical_image.jpg",
  "message": "What is this skin condition?",
  "session_id": "unique_session_id"
}
```

### **Response Format**
```json
{
  "reply": "AI-generated medical response based on selected agent"
}
```

---

## 🔧 Troubleshooting

### **Common Issues**

#### **Backend Won't Start**
```bash
# Check Python version
python --version  # Should be 3.8+

# Reinstall dependencies
pip install -r requirements.txt

# Check .env file exists with API keys
cd backend && ls -la .env
```

#### **Frontend Won't Load**
```bash
# Check Node.js version
node --version    # Should be 16+
npm --version

# Reinstall dependencies
cd frontend && npm install

# Clear npm cache if needed
npm cache clean --force
```

#### **API Connection Issues**
- **Backend not running**: Ensure `http://127.0.0.1:8000` is accessible
- **CORS errors**: Check browser console, restart backend server
- **API key errors**: Verify `.env` file contains valid Groq and Tavily keys

#### **Image Upload Problems**
- **File size**: Maximum 10MB supported
- **File format**: JPG, PNG, GIF, BMP only
- **Upload flow**: Images should disappear from input immediately when sent

#### **UI/UX Issues**
- **Typing animation**: New messages should animate, refresh should show all instantly
- **Markdown rendering**: Headers should be bold, not show raw ### symbols  
- **Scroll behavior**: New responses should show from top, not auto-scroll to bottom

### **Development Tips**

#### **Frontend Development**
```bash
# Start with hot reload
npm start

# Check for linting errors
npm run lint

# Build for production
npm run build
```

#### **Backend Development**
```bash
# Start with auto-reload
uvicorn main:app --reload

# Check API docs
# Visit: http://127.0.0.1:8000/docs

# Test individual agents
cd agents && python test.py
```

---

## 🎯 Project Highlights

### **Advanced UI Features Implemented**
- ✅ **ChatGPT-style Interface**: Professional chat design with smooth transitions
- ✅ **Smart Typing Animation**: Time-based detection prevents replay on refresh  
- ✅ **Professional Markdown**: Bold headers and clean formatting for medical content
- ✅ **Seamless Image Upload**: Files move cleanly from input to conversation
- ✅ **Session Persistence**: Conversation history maintained across browser sessions

### **Multi-Agent Intelligence**
- ✅ **Intelligent Routing**: Automatically selects best AI agent for each query type
- ✅ **RAG Integration**: Search through medical literature and research papers
- ✅ **Vision Analysis**: AI-powered medical image interpretation
- ✅ **Real-time Research**: Access latest medical information via web search
- ✅ **Content Safety**: Built-in guardrails for appropriate medical discussions

---

This Medical Assistant provides an intelligent, multi-modal approach to medical query processing, ensuring users receive appropriate responses through the most suitable AI agent for their specific needs.