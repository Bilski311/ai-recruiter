import Card from "@/components/shared/Card";
import { faHtml5 } from "@fortawesome/free-brands-svg-icons/faHtml5";
import { faSquareJs } from "@fortawesome/free-brands-svg-icons/faSquareJs";
import { faCss3Alt } from "@fortawesome/free-brands-svg-icons/faCss3Alt";

interface Props {
  className?: string;
}

function Sets({ className }: Props) {
  return (
    <section className={`${className}`}>
      <div className="max-w-6xl mx-auto">
        <h2 className="text-4xl font-bold text-center mb-6">Flashcard Sets</h2>
        <hr className="border-gray-300 mb-8" />
        <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
          <Card
            className={"mx-5"}
            title={"HTML"}
            description={
              "Description: HTML is the standard markup language used to structure content on the web. It forms the backbone of web pages by defining elements such as headings, paragraphs, lists, links, images, and more. HTML uses a system of tags to create and organize the structure of a web page."
            }
            icon={faHtml5}
            iconClassName={"text-orange-600"}
          />
          <Card
            className={"mx-5"}
            title={"JavaScript"}
            description={
              "JavaScript is a high-level, versatile programming language that enables web developers to create interactive and dynamic web applications. It is responsible for adding interactivity, animations, and advanced functionality to websites. JavaScript is widely supported by all major web browsers and is an essential skill for modern web development."
            }
            icon={faSquareJs}
            iconClassName={"text-yellow-500"}
          />
          <Card
            className={"mx-5"}
            title={"CSS"}
            description={
              "CSS is a stylesheet language used to control the appearance and formatting of web pages. It allows developers to style HTML elements by defining properties such as color, font, layout, and spacing. CSS helps to separate the content structure (HTML) from the visual presentation, making it easier to maintain and scale web designs."
            }
            icon={faCss3Alt}
            iconClassName={"text-blue-600"}
          />
        </div>
      </div>
    </section>
  );
}

export default Sets;
