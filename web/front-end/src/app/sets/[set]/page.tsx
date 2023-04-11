import { Set, SetOptions } from "@/objectAssertions/setOptions";
import { notFound } from "next/navigation";
import FlashcardContainer from "@/app/sets/FlashcardContainer";

interface props {
  params: {
    set: Set;
  };
}

function Set({ params: { set } }: props) {
  if (!Object.values(SetOptions).includes(set)) return notFound();
  return (
    <>
      <FlashcardContainer />
    </>
  );
}

export default Set;
