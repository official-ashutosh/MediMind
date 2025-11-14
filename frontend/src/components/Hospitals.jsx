import React, { useEffect, useState } from "react";
import Navbar from "./Navbar"; // Import the updated Navbar component
import hospitalImage from "../assets/hospital.jpg"; // Default hospital image
import Squares from "./Squares"; // Import Squares background component


const BASE_URL = import.meta.env.VITE_BASE_URL;

const HospitalCard = ({ hospital }) => {
  return (
    <div className="backdrop-blur-lg bg-white/90 shadow-xl rounded-2xl border border-gray-200 p-4 relative hover:shadow-2xl transition-shadow duration-300">
      <img
        src={hospital.image || hospitalImage} // Use API image or default one
        alt={hospital.name}
        className="w-full h-48 object-cover rounded-xl"
      />
      <div className="p-4">
        <h2 className="text-xl font-semibold text-[#0d47a1]">{hospital.name}</h2>
        <p className="text-gray-700">{hospital.address}</p>
        <div className="flex items-center gap-2 mt-2">
          <span className="w-5 h-5">📞</span>
          <span className="text-gray-800 font-medium">{hospital.contact_no}</span>
        </div>
        <a
          href={hospital.map_link || `https://www.google.com/maps?q=${hospital.name}`}
          target="_blank"
          rel="noopener noreferrer"
          className="mt-4 flex items-center gap-2 text-white bg-[#1976d2] px-4 py-2 rounded-lg hover:bg-[#0d47a1]"
        >
          <span className="w-5 h-5">📍</span> View on Map
        </a>
      </div>
    </div>
  );
};

const HospitalList = () => {
  const [hospitals, setHospitals] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    fetch(`${BASE_URL}/hospitals/`)
      .then((response) => {
        if (!response.ok) {
          throw new Error("Failed to fetch hospitals");
        }
        return response.json();
      })
      .then((data) => {
        setHospitals(data);
        setLoading(false);
      })
      .catch((error) => {
        console.error("Error fetching hospitals:", error);
        setError(error.message);
        setLoading(false);
      });
  }, []);

  return (
    <div className="relative min-h-screen flex flex-col bg-transparent p-2">
      {/* Squares Background - Ensure it is visible */}
      <div className="absolute inset-0 w-full h-full z-0 pointer-events-none">
        <Squares 
          speed={0.2} 
          squareSize={40}
          direction="diagonal" // up, down, left, right, diagonal
          borderColor="#1976d2"
          hoverFillColor="#0d47a1"
        />
      </div>
      
      {/* Full-width Navbar - Passing the active page prop */}
      {/* <Navbar className="w-full" /> */}
      
      {/* Content container - Centered */}
      <div className="flex flex-col items-center w-full z-10">
        {/* Loading and Error States */}
        {loading ? (
          <p className="text-center text-lg font-semibold mt-10 text-[#1976d2]">Loading hospitals...</p>
        ) : error ? (
          <p className="text-center text-red-600 font-semibold mt-10">{error}</p>
        ) : (
          <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6 p-6 max-w-7xl mx-auto">
            {hospitals.map((hospital, index) => (
              <HospitalCard key={index} hospital={hospital} />
            ))}
          </div>
        )}
      </div>
    </div>
  );
};

export default HospitalList;