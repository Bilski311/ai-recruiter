import Header from "@/app/Header";
import "../styles/globals.css";
import "../styles/animations.css";
import Footer from "@/app/Footer";

export const metadata = {
  title: "My next.js app",
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html>
      <body className="flex flex-col min-h-screen">
        <Header />
        <div className="flex-1">{children}</div>
        <Footer />
      </body>
    </html>
  );
}
