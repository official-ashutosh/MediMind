import React, { useState, useEffect, useRef } from "react";
import axios from "axios";
import { Send, Loader, RefreshCw } from "lucide-react";

const BASE_URL = import.meta.env.VITE_BASE_URL;


const ChatBot = () => {
  const [sessionId, setSessionId] = useState(null);
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState("");
  const [isLoading, setIsLoading] = useState(false);
  const messagesEndRef = useRef(null);

  useEffect(() => {
    startChat();
    initializeStars();
  }, []);

  useEffect(() => {
    scrollToBottom();
  }, [messages]);

  const initializeStars = () => {
    const starContainer = document.getElementById("star-container");
    if (!starContainer) return;

    const starCount = 100;
    
    for (let i = 0; i < starCount; i++) {
      const star = document.createElement("div");
      star.classList.add("star");
      
      // Random position
      star.style.top = `${Math.random() * 100}%`;
      star.style.left = `${Math.random() * 100}%`;
      
      // Random size
      const size = Math.random() * 2 + 1;
      star.style.width = `${size}px`;
      star.style.height = `${size}px`;
      
      // Random animation delay
      star.style.animationDelay = `${Math.random() * 10}s`;
      
      starContainer.appendChild(star);
    }
  };

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: "smooth" });
  };

  const startChat = async () => {
    const newSessionId = Date.now().toString();
    setSessionId(newSessionId);
    setIsLoading(true);

    try {
      const response = await axios.post(`${BASE_URL}/prediction/start_chat`, { session_id: newSessionId });
      setMessages([{ sender: "bot", text: response.data.message }]);
    } catch (error) {
      console.error("Error starting chat:", error);
      setMessages([{ 
        sender: "bot", 
        text: "Sorry, I couldn't connect. Please try refreshing the page." 
      }]);
    } finally {
      setIsLoading(false);
    }
  };

  const sendMessage = async () => {
    if (!input.trim() || isLoading) return;

    const userMessage = input.trim();
    setMessages((prev) => [...prev, { sender: "user", text: userMessage }]);
    setInput("");
    setIsLoading(true);

    try {
      const response = await axios.post(`${BASE_URL}/prediction/process_message`, {
        session_id: sessionId,
        user_message: userMessage
      });

      setMessages((prev) => [...prev, { sender: "bot", text: response.data.message }]);
    } catch (error) {
      console.error("Error sending message:", error);
      setMessages((prev) => [
        ...prev, 
        { sender: "bot", text: "Sorry, something went wrong. Please try again." }
      ]);
    } finally {
      setIsLoading(false);
    }
  };

  const handleKeyPress = (e) => {
    if (e.key === "Enter") {
      sendMessage();
    }
  };

  return (
    <div className="relative h-screen w-full overflow-hidden bg-black">
      {/* Space animation background */}
      <div id="star-container" className="absolute inset-0 z-0"></div>
      
      <div className="relative z-10 flex flex-col items-center justify-center h-full p-4">
        <div className="w-full max-w-2xl">
          <h1 className="text-3xl font-bold text-center mb-6 text-white">
            🩺 Health Diagnosis Assistant
          </h1>
          
          {/* Chat container with glassmorphism effect */}
          <div className="bg-white bg-opacity-20 backdrop-blur-lg rounded-lg shadow-lg overflow-hidden border border-white border-opacity-30">
            {/* Chat messages */}
            <div className="h-96 overflow-y-auto p-4 space-y-4 bg-white bg-opacity-10">
              {messages.map((msg, index) => (
                <div 
                  key={index} 
                  className={`flex ${msg.sender === "user" ? "justify-end" : "justify-start"}`}
                >
                  <div 
                    className={`max-w-xs md:max-w-md px-4 py-2 rounded-lg shadow-md ${
                      msg.sender === "user" 
                        ? "bg-[#1976d2] text-white rounded-br-none" 
                        : "bg-white text-gray-800 rounded-bl-none border border-gray-200"
                    }`}
                  >
                    {msg.text}
                  </div>
                </div>
              ))}
              {isLoading && (
                <div className="flex justify-start">
                  <div className="bg-white text-gray-800 px-4 py-2 rounded-lg rounded-bl-none flex items-center shadow-md border border-gray-200">
                    <Loader className="w-4 h-4 mr-2 animate-spin text-[#1976d2]" />
                    Thinking...
                  </div>
                </div>
              )}
              <div ref={messagesEndRef} />
            </div>
            
            {/* Input area */}
            <div className="p-4 border-t border-gray-200 bg-white">
              <div className="flex">
                <input
                  type="text"
                  value={input}
                  onChange={(e) => setInput(e.target.value)}
                  onKeyPress={handleKeyPress}
                  placeholder="Describe your symptoms..."
                  className="flex-grow px-4 py-2 bg-gray-50 border border-gray-300 rounded-l-lg focus:outline-none focus:ring-2 focus:ring-[#1976d2] text-gray-800 placeholder-gray-500"
                  disabled={isLoading}
                />
                <button
                  onClick={sendMessage}
                  disabled={isLoading || !input.trim()}
                  className="px-4 py-2 bg-[#1976d2] hover:bg-[#0d47a1] text-white rounded-r-lg transition-colors duration-200 disabled:opacity-50"
                >
                  <Send className="w-5 h-5" />
                </button>
              </div>
            </div>
          </div>
          
          {/* Reset button */}
          <div className="mt-4 flex justify-center">
            <button
              onClick={startChat}
              className="flex items-center px-4 py-2 bg-white bg-opacity-90 hover:bg-opacity-100 border border-gray-200 rounded-lg text-gray-800 transition-colors duration-200 shadow-md"
            >
              <RefreshCw className="w-4 h-4 mr-2" />
              Reset Conversation
            </button>
          </div>
        </div>
      </div>
      
      {/* CSS for the space animation */}
      <style jsx>{`
        .star {
          position: absolute;
          background-color: #fff;
          border-radius: 50%;
          animation: twinkle 5s infinite;
        }
        
        @keyframes twinkle {
          0% { opacity: 0.3; }
          50% { opacity: 1; }
          100% { opacity: 0.3; }
        }
      `}</style>
    </div>
  );
};

export default ChatBot;