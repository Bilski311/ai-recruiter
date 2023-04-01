import Header from "@/app/Header";
import "../styles/globals.css";
import "../styles/animations.css";

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
      <body>
        <Header />
        {children}
      </body>
    </html>
  );
}
