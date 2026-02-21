import { useState } from "react";

type Props = {
  onSend: (text: string) => void;
};

const ChatInput = ({ onSend }: Props) => {
  const [input, setInput] = useState<string>("");

  const handleSend = () => {
    if (!input.trim()) return;
    onSend(input);
    setInput("");
  };

  return (
    <div style={{ display: "flex", marginTop: "10px" }}>
      <input
        style={{ flex: 1, padding: "10px" }}
        value={input}
        onChange={(e) => setInput(e.target.value)}
        placeholder="Ask something..."
      />
      <button onClick={handleSend} style={{ padding: "10px" }}>
        Send
      </button>
    </div>
  );
};

export default ChatInput;