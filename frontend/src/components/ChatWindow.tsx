import { useState } from "react";
import ChatMessage from "./ChatMessage";
import ChatInput from "./ChatInput";
import { sendMessage } from "../services/api";

type Message = {
  sender: "user" | "bot";
  text: string;
};

const ChatWindow = () => {
  const [messages, setMessages] = useState<Message[]>([]);

  const handleSend = async (text: string) => {
    const userMessage: Message = { sender: "user", text };
    setMessages((prev) => [...prev, userMessage]);

    try {
      const botReply = await sendMessage(text);

      const botMessage: Message = { sender: "bot", text: botReply };
      setMessages((prev) => [...prev, botMessage]);
    } catch {
      const errorMessage: Message = {
        sender: "bot",
        text: "Error connecting to server.",
      };
      setMessages((prev) => [...prev, errorMessage]);
    }
  };

  return (
    <div style={{ width: "600px", margin: "auto", marginTop: "40px" }}>
      <h2>TCS RAG Chatbot</h2>

      <div
        style={{
          border: "1px solid #ccc",
          padding: "10px",
          height: "400px",
          overflowY: "auto",
        }}
      >
        {messages.map((msg, index) => (
          <ChatMessage key={index} message={msg} />
        ))}
      </div>

      <ChatInput onSend={handleSend} />
    </div>
  );
};

export default ChatWindow;