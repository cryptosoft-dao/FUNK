import { useState } from "react";
import Earn from "./pages/Earn";
import pageTypes from "./constants/pageTypes";
import Loading from "./components/Loading";
import Tasks from "./pages/Tasks";
import Team from "./pages/Team";
import Navbar from "./components/Navbar";

function App() {
  const [page, setPage] = useState(pageTypes.loading)
  return (
    <>
      {page === pageTypes.loading && (<Loading setPage={setPage} />)}
      {page !== pageTypes.loading && (<Earn setPage={setPage} />)}
      {page === pageTypes.tasks && (<Tasks setPage={setPage} />)}
      {page === pageTypes.team && (<Team setPage={setPage} />)}
      {page !== pageTypes.loading && (<Navbar setPage={setPage} />)}
    </>
  );
}

export default App;
