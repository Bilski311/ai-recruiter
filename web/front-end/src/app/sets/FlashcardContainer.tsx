import Flashcard from "@/app/sets/[set]/Flashcard";
import { faBrain } from "@fortawesome/free-solid-svg-icons/faBrain";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faBook } from "@fortawesome/free-solid-svg-icons/faBook";

function FlashcardContainer() {
  return (
    <>
      <div className={"flex flex-row justify-center w-full"}>
        <Flashcard question={"test"} answer={"dupa"} className={"m-10"} />
      </div>
      <div className={"flex flex-row justify-center w-full"}>
        <div className="w-20 h-20 rounded-full border-4 border-red-700 mx-10 flex justify-center text-red-700 hover:bg-red-700 hover:text-white cursor-pointer">
          <FontAwesomeIcon
            icon={faBook}
            style={{ width: "2rem", height: "auto" }}
          />
        </div>
        <div className="w-20 h-20 rounded-full border-4 border-green-700 mx-10 flex justify-center text-green-700 hover:bg-green-700 hover:text-white cursor-pointer">
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
