"use client";

import Flashcard from "@/app/sets/[set]/Flashcard";
import { faBrain } from "@fortawesome/free-solid-svg-icons/faBrain";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faBook } from "@fortawesome/free-solid-svg-icons/faBook";
import { useState } from "react";

function FlashcardContainer() {
  const [content, setContent] = useState("Test question");

  return (
    <>
      <div
        className={"flex flex-row justify-center w-full slide-in"}
        key={content}
      >
        <Flashcard question={content} answer={"dupa"} className={"m-10"} />
      </div>
      <div className={"flex flex-row justify-center w-full animate-fade-in"}>
        <div
          className="w-20 h-20 rounded-full border-4 border-red-700 mx-10 flex justify-center text-red-700 hover:bg-red-700 hover:text-white cursor-pointer pulse"
          onClick={() =>
            setContent((prevState) =>
              prevState === "Test question"
                ? "Test question 1"
                : "Test question"
            )
          }
        >
          <FontAwesomeIcon
            icon={faBook}
            style={{ width: "2rem", height: "auto" }}
          />
        </div>
        <div className="w-20 h-20 rounded-full border-4 border-green-700 mx-10 flex justify-center text-green-700 hover:bg-green-700 hover:text-white cursor-pointer pulse">
          <FontAwesomeIcon
            icon={faBrain}
            style={{ width: "3rem", height: "auto" }}
          />
        </div>
      </div>
    </>
  );
}

export default FlashcardContainer;
