import { useEffect } from "react";

function App() {
  useEffect(() => {
    fetch("/movies")
      .then((r) => r.json())
      .then((data) => console.log(data));
  }, []);

  return <h1>Check the console for a list of movies!</h1>;
}

export default App;