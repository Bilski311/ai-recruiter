import Flashcard from "@/app/sets/[set]/Flashcard";

function FlashcardContainer() {
  return (
    <>
      <div className={"flex flex-row justify-center w-full"}>
        <Flashcard question={"test"} answer={"dupa"} className={"m-10"} />
      </div>
      <div className={"mt-10 flex flex-row justify-around w-full"}>
        <h1>Dupa</h1>
        <h1>Dupa</h1>
      </div>
    </>
  );
}

export default FlashcardContainer;
