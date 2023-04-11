"use client";

import { useState } from "react";
import "../../../styles/flashcard.css";

interface FlashcardProps {
  question: string;
  answer: string;
  className?: string;
}

function Flashcard({ question, answer, className }: FlashcardProps) {
  const [isFlipped, setIsFlipped] = useState(false);

  const handleClick = () => {
    setIsFlipped(!isFlipped);
  };

  return (
    <div
      className={`flash-card ${isFlipped ? "flipped" : ""} ${className}`}
      onClick={handleClick}
    >
      <div className="flash-card-inner">
        <div className="flash-card-front">
          <p>{question}</p>
        </div>
        <div className="flash-card-back">
          <p>{answer}</p>
        </div>
      </div>
    </div>
  );
}

export default Flashcard;
