import { Set, SetOptions } from "@/objectAssertions/setOptions";
import { notFound } from "next/navigation";

interface props {
  params: {
    set: Set;
  };
}

function Set({ params: { set } }: props) {
  if (!Object.values(SetOptions).includes(set)) return notFound();
  return <div>{set}</div>;
}

export default Set;
