import Card from "@/components/shared/Card";
import { faHtml5 } from "@fortawesome/free-brands-svg-icons/faHtml5";
import { faSquareJs } from "@fortawesome/free-brands-svg-icons/faSquareJs";
import { faCss3Alt } from "@fortawesome/free-brands-svg-icons/faCss3Alt";

function Home() {
  return (
    <>
      <main className="bg-gray-100">
        <section className="py-20 px-6">
          <div className="max-w-4xl mx-auto text-center">
            <h1 className="text-5xl font-bold text-gray-800 mb-6">
              Welcome to the Future of Job Searching
            </h1>
            <p className="text-xl text-gray-600 mb-10">
              Find your dream job with our advanced AI-powered job matching
              system.
            </p>
            <button className="bg-gradient-to-r from-indigo-600 to-purple-500 text-white font-semibold py-3 px-6 rounded focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500 pulse">
              Get Started
            </button>
          </div>
        </section>

        <section className="py-20 px-6">
          <div className="max-w-6xl mx-auto grid grid-cols-1 md:grid-cols-3 gap-8">
            <Card
              title={"HTML"}
              description={
                "Description: HTML is the standard markup language used to structure content on the web. It forms the backbone of web pages by defining elements such as headings, paragraphs, lists, links, images, and more. HTML uses a system of tags to create and organize the structure of a web page."
              }
              icon={faHtml5}
              iconClassName={"text-orange-600"}
            />
            <Card
              title={"JavaScript"}
              description={
                "JavaScript is a high-level, versatile programming language that enables web developers to create interactive and dynamic web applications. It is responsible for adding interactivity, animations, and advanced functionality to websites. JavaScript is widely supported by all major web browsers and is an essential skill for modern web development."
              }
              icon={faSquareJs}
              iconClassName={"text-yellow-500"}
            />
            <Card
              title={"CSS"}
              description={
                "CSS is a stylesheet language used to control the appearance and formatting of web pages. It allows developers to style HTML elements by defining properties such as color, font, layout, and spacing. CSS helps to separate the content structure (HTML) from the visual presentation, making it easier to maintain and scale web designs."
              }
              icon={faCss3Alt}
              iconClassName={"text-blue-600"}
            />
          </div>
        </section>
      </main>
    </>
  );
}

export default Home;
