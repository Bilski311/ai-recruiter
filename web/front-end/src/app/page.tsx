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
            <div className="bg-white rounded-lg p-8 shadow-md text-center">
              <h2 className="text-2xl font-bold mb-4">Advanced AI Matching</h2>
              <p>
                Our AI-driven algorithms analyze your skills and preferences to
                find the perfect job for you.
              </p>
            </div>
            <div className="bg-white rounded-lg p-8 shadow-md text-center">
              <h2 className="text-2xl font-bold mb-4">Fast and Efficient</h2>
              <p>
                Save time and effort by applying to multiple jobs at once with
                our streamlined application process.
              </p>
            </div>
            <div className="bg-white rounded-lg p-8 shadow-md text-center">
              <h2 className="text-2xl font-bold mb-4">
                Expansive Job Database
              </h2>
              <p>
                Access thousands of job listings from top employers across a
                wide range of industries.
              </p>
            </div>
          </div>
        </section>
      </main>
    </>
  );
}

export default Home;
