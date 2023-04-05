import React from "react";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { IconDefinition } from "@fortawesome/fontawesome-svg-core";

export interface ClickableCardProps {
  title: string;
  description: string;
  icon: IconDefinition;
  iconClassName: string;
  onClick: () => void;
  className?: string;
}

function ClickableCard({
  title,
  description,
  icon,
  iconClassName,
  onClick,
  className,
}: ClickableCardProps) {
  return (
    <div
      onClick={onClick}
      className={`bg-white rounded-lg shadow-md text-center p-8 hover:cursor-pointer hover:shadow-lg hover:bg-gray-800 hover:text-white ${className}`}
    >
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

export default ClickableCard;
