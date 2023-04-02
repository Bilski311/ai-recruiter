import React from "react";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { IconDefinition } from "@fortawesome/fontawesome-svg-core";

interface Props {
  title: string;
  description: string;
  icon: IconDefinition;
  iconClassName: string;
}

function Card({ title, description, icon, iconClassName }: Props) {
  return (
    <div className="bg-white rounded-lg shadow-md text-center p-8 hover:cursor-pointer hover:shadow-lg hover:bg-gray-800 hover:text-white">
      <div className="flex justify-center items-center mb-4">
        <FontAwesomeIcon
          icon={icon}
          className={`mr-4 ${iconClassName}`}
          style={{ width: "1.5rem", height: "auto" }}
        />
        <h2 className="text-2xl font-bold">{title}</h2>
      </div>
      <p>{description}</p>
    </div>
  );
}

export default Card;
