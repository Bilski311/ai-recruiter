interface Props {
  className?: string;
}

function Footer({ className }: Props) {
  return (
    <footer className={`bg-gray-800 py-12 px-6 ${className}`}>
      <div className="max-w-4xl mx-auto text-center">
        <p className="text-white font-semibold text-xl mb-2">
          Futuristic Job Market
        </p>
        <p className="text-gray-400">
          &copy; {new Date().getFullYear()} Futuristic Job Market. All rights
          reserved.
        </p>
      </div>
    </footer>
  );
}

export default Footer;
