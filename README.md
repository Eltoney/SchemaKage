# 🌀 SchemaKage — Project Phases

SchemaKage is an AI-powered database assistant designed to simplify schema design, data generation, and query handling across SQL and NoSQL databases.  
This document outlines the **4-phase roadmap** for SchemaKage, showing both immediate goals and long-term vision.  

---

## 📍 Phase 1 — Core SQL Agent (Current Focus)
**🎯 Goal:** Build the foundation of SchemaKage with PostgreSQL support.  

### ✅ Features
1. Take a schema definition (user-provided or generated) and generate **sample data**.  
2. Generate **SQL commands** to create tables from the schema.  
   - Start with **PostgreSQL**.  
   - Support adding new tables to existing databases.  
3. **Dockerize** the project for easy setup and portability.  
4. Integrate with an **LLM (API-based)** for natural language assistance in schema creation and query generation.  

---

## 📍 Phase 2 — NoSQL Support
**🎯 Goal:** Extend SchemaKage to work with **NoSQL databases** (starting with MongoDB).  

### ✅ Features
1. Support schema definitions and data generation for NoSQL.  
2. Auto-generate database creation and insertion commands for **MongoDB**.  
3. Implement a **Factory Design Pattern** to abstract schema parsing and data generation depending on DB type (SQL vs NoSQL).  
4. Let users **choose SQL or NoSQL** at the start of the workflow.  

---

## 📍 Phase 3 — Schema & Relationship Visualization
**🎯 Goal:** Help users **visualize database schemas** and relationships across selected tables.  

### ✅ Features
1. Extract schema and relationship info from selected tables.  
2. Generate **ERD-style diagrams** (Entity-Relationship Diagrams).  
3. Provide a natural language interface to ask:  
   - “Show me relationships between users and orders.”  
   - “Generate a diagram for my ecommerce schema.”  
4. Support exporting diagrams (**PNG/SVG**).  

---

## 📍 Phase 4 — Data Mapping & Smart Insertion
**🎯 Goal:** Make it easier to **map data to existing tables** intelligently.  

### ✅ Features
1. Take user-provided data and **map it to existing tables** based on schema.  
2. Suggest mapping automatically (e.g., “this CSV column fits into `users.email`).  
3. Allow the user to **confirm/override mappings**.  
4. Insert mapped data into existing tables.  

---

## 🌟 Long-Term Vision
SchemaKage will evolve into a **universal database assistant**, bridging human language and database management — from schema design to visualization, data mapping, and multi-database integration.  

---

⚡ **Next Step:** Build **Phase 1 → PostgreSQL Core Agent**.  
