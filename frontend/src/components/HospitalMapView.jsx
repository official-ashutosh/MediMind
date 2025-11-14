import React, { useEffect, useState } from "react";
import { Map, Marker, Overlay } from "pigeon-maps";

const HospitalMapView = () => {
  const [hospitals, setHospitals] = useState([]);
  const [hoveredHospital, setHoveredHospital] = useState(null);
  const BASE_URL = import.meta.env.VITE_BASE_URL;

  useEffect(() => {
    fetch(`${BASE_URL}/hospitals/`)
      .then((response) => response.json())
      .then((data) => {
        console.log("Fetched hospitals:", data);
        setHospitals(data);
      })
      .catch((error) => console.error("Error fetching hospitals:", error));
  }, []);

  // Center on Prayagraj (Allahabad): 25.4358° N, 81.8463° E
  const mapCenter = [25.4358, 81.8463];

  return (
    <div className="w-full h-full rounded-xl shadow-lg overflow-hidden">
      <Map defaultCenter={mapCenter} defaultZoom={12} height={500}>
        {hospitals && hospitals.length > 0 && hospitals.map((hospital) => {
          // Check if latitude and longitude exist
          if (!hospital.latitude || !hospital.longitude) {
            console.warn("Hospital missing coordinates:", hospital.name);
            return null;
          }
          
          return (
            <Marker
              key={hospital._id}
              width={40}
              anchor={[hospital.latitude, hospital.longitude]}
              onMouseOver={() => setHoveredHospital(hospital)}
              onMouseOut={() => setHoveredHospital(null)}
            />
          );
        })}

        {hoveredHospital && hoveredHospital.latitude && hoveredHospital.longitude && (
          <Overlay
            anchor={[hoveredHospital.latitude, hoveredHospital.longitude]}
            offset={[0, -30]}
          >
            <div className="bg-white p-3 rounded-md shadow-lg text-xs text-black max-w-xs border-2 border-blue-500">
              <strong className="text-sm">{hoveredHospital.name}</strong>
              <p className="mt-1">{hoveredHospital.address}, {hoveredHospital.city}</p>
              <p className="mt-1">📞 {hoveredHospital.contact_no}</p>
            </div>
          </Overlay>
        )}
      </Map>
    </div>
  );
};

export default HospitalMapView;
