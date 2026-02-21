type Message = {
  sender: "user" | "bot";
  text: string;
};

type Props = {
  message: Message;
};

const ChatMessage = ({ message }: Props) => {
  return (
    <div
      style={{
        textAlign: message.sender === "user" ? "right" : "left",
        margin: "10px 0",
      }}
    >
      <span
        style={{
          padding: "10px",
          borderRadius: "12px",
          backgroundColor:
            message.sender === "user" ? "#4CAF50" : "#f1f1f1",
          color: message.sender === "user" ? "white" : "black",
          display: "inline-block",
          maxWidth: "70%",
        }}
      >
        {message.text}
      </span>
    </div>
  );
};

export default ChatMessage;