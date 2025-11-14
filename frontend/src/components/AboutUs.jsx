


import React, { useState, useEffect, useRef } from 'react';
import Squares from './Squares';
import { Link } from 'react-router-dom'
import ashuImage from "../assets/ashu.jpeg";
import hmtImage from "../assets/hmt.jpeg";
import deepakImage from "../assets/deepak.jpeg";
import pooniImage from "../assets/pooni.jpeg"; // Using doctor image for 4th contributor

const AboutUs = () => {
  const [isHovering, setIsHovering] = useState(false);
  const cratesRef = useRef(null);
  const animationRef = useRef(null);

  useEffect(() => {
    if (!cratesRef.current) return;

    let angle = 0;
    const centerX = 100;
    const centerY = 100;
    const radius = 60;
    const crateElements = cratesRef.current.querySelectorAll('.crate');

    const animate = () => {
      if (isHovering) {
        cancelAnimationFrame(animationRef.current);
        return;
      }

      crateElements.forEach((crate, index) => {
        // Position crates in a circular formation (120° apart)
        const crateAngle = angle + (index * (Math.PI * 2) / 3);
        const x = centerX + Math.cos(crateAngle) * radius;
        const y = centerY + Math.sin(crateAngle) * radius;

        // Apply only translation without rotation
        crate.style.transform = `translate(${x}px, ${y}px)`;
      });

      angle += 0.005;
      animationRef.current = requestAnimationFrame(animate);
    };

    animate();

    return () => {
      cancelAnimationFrame(animationRef.current);
    };
  }, [isHovering]);

  return (
    <div className="relative h-screen overflow-hidden">
      {/* Background squares */}
      <div style={{ position: "absolute", top: 0, left: 0, width: "100%", height: "100%", zIndex: -1 }}>
        <Squares 
          speed={0.2} 
          squareSize={40}
          direction='diagonal'
          borderColor='#1976d2'
          hoverFillColor='#0d47a1'
        />
      </div>

      {/* Light gradient overlay */}
      <div className="absolute inset-0 bg-gradient-to-br from-blue-50/30 to-teal-50/30 z-0"></div>

      {/* Main content */}
      <div className="relative z-10 h-screen flex flex-col p-6">
        <div className="max-w-7xl mx-auto w-full flex-1 flex flex-col">
          {/* Header */}
          <div className="flex flex-col items-center mb-6">
            <h1 className="text-4xl font-extrabold text-[#0d47a1] mb-2 drop-shadow-lg bg-white/90 px-6 py-2 rounded-xl shadow-xl">About Us</h1>
            <div className="w-24 h-1 bg-gradient-to-r from-[#0d47a1] via-[#1976d2] to-[#00897b] rounded-full"></div>
          </div>

          {/* Contributors Section at Top */}
          <div className="mb-4">
            <div className="relative overflow-hidden group">
              <div className="absolute inset-0 bg-gradient-to-br from-[#1976d2] to-[#00897b] rounded-2xl shadow-xl"></div>
              <div className="relative p-3 text-white z-10 flex items-center justify-between">
                <div className="flex-1">
                  <h2 className="text-xl font-bold mb-1">Our Contributors</h2>
                  <p className="text-sm leading-relaxed">
                    <span className="font-semibold">Ashutosh, Deepak, Hemant, Poonam</span> - guided by <span className="font-semibold">KP Singh</span>
                  </p>
                </div>
                
                {/* Team Photos */}
                <div className="flex gap-2 ml-4">
                  {[
                    { link: "https://www.linkedin.com/in/ashusolver/", img: ashuImage, name: "Ashutosh" },
                    { link: "https://www.linkedin.com/in/deepak/", img: deepakImage, name: "Deepak" },
                    { link: "https://www.linkedin.com/in/ashusolver/", img: hmtImage, name: "Hemant" },
                    { link: "https://www.linkedin.com/in/ashusolver/", img: pooniImage, name: "Poonam" }
                  ].map((person, idx) => (
                    <a 
                      key={idx}
                      href={person.link}
                      target="_blank"
                      rel="noopener noreferrer"
                      className="w-14 h-14 rounded-lg shadow-lg transition-all duration-300 hover:scale-110 hover:z-50 flex items-center justify-center overflow-hidden border-2 border-white relative group"
                    >
                      <img 
                        src={person.img} 
                        alt={person.name} 
                        className="w-full h-full object-cover"
                      />
                      <div className="absolute inset-0 bg-gradient-to-t from-black/70 to-transparent opacity-0 group-hover:opacity-100 transition-opacity flex items-end justify-center pb-1">
                        <p className="text-white font-bold text-[10px] drop-shadow-lg">{person.name}</p>
                      </div>
                    </a>
                  ))}
                </div>
              </div>
            </div>
          </div>

          {/* Content Sections - Compact Grid */}
          <div className="grid md:grid-cols-3 gap-3 max-h-[35vh]">
            {/* Our Story */}
            <div className="relative group">
              <div className="absolute inset-0 bg-gradient-to-r from-[#0d47a1] to-[#00897b] rounded-2xl shadow-xl transform transition-all duration-300 group-hover:scale-[1.02]"></div>
              <div className="relative p-4 z-10 h-full flex flex-col">
                <h2 className="text-xl font-bold mb-3 text-white">Our Story</h2>
                <p className="text-sm font-bold mb-2 text-yellow-300">AI-Powered Health, One Step Ahead.</p>
                <p className="text-sm leading-relaxed text-white">
                  MediMind is revolutionizing healthcare with AI-driven disease prediction, connecting users to accurate diagnoses faster and smarter.
                </p>
              </div>
            </div>

            {/* Our Mission */}
            <div className="relative group">
              <div className="absolute inset-0 bg-gradient-to-bl from-[#1976d2] to-[#0d47a1] rounded-2xl shadow-xl transform transition-all duration-300 group-hover:scale-[1.02]"></div>
              <div className="relative p-4 z-10 h-full flex flex-col">
                <h2 className="text-xl font-bold mb-3 text-white">Our Mission</h2>
                <p className="text-sm leading-relaxed text-white">
                  We're on a mission to revolutionize how people interact with healthcare technology, making medical predictions accessible to everyone.
                </p>
              </div>
            </div>

            {/* Our Values */}
            <div className="relative group">
              <div className="absolute inset-0 bg-gradient-to-l from-[#00897b] to-[#0d47a1] rounded-2xl shadow-xl transform transition-all duration-300 group-hover:scale-[1.02]"></div>
              <div className="relative p-4 z-10 h-full flex flex-col">
                <h2 className="text-xl font-bold mb-3 text-white">Our Values</h2>
                <div className="grid grid-cols-1 gap-2 text-sm">
                  <div className="flex items-center space-x-2 bg-white/10 p-2 rounded-lg backdrop-blur-sm">
                    <div className="w-2 h-2 rounded-full bg-yellow-300 flex-shrink-0"></div>
                    <span className="text-white">Innovation</span>
                  </div>
                  <div className="flex items-center space-x-2 bg-white/10 p-2 rounded-lg backdrop-blur-sm">
                    <div className="w-2 h-2 rounded-full bg-yellow-300 flex-shrink-0"></div>
                    <span className="text-white">Integrity</span>
                  </div>
                  <div className="flex items-center space-x-2 bg-white/10 p-2 rounded-lg backdrop-blur-sm">
                    <div className="w-2 h-2 rounded-full bg-yellow-300 flex-shrink-0"></div>
                    <span className="text-white">Impact</span>
                  </div>
                  <div className="flex items-center space-x-2 bg-white/10 p-2 rounded-lg backdrop-blur-sm">
                    <div className="w-2 h-2 rounded-full bg-yellow-300 flex-shrink-0"></div>
                    <span className="text-white">Inclusivity</span>
                  </div>
                </div>
              </div>
            </div>
          </div>

          {/* Contact Section at Bottom */}
          <div className="mt-4">
            <div className="relative overflow-hidden group">
              <div className="absolute inset-0 bg-gradient-to-br from-[#1976d2] to-[#00897b] rounded-2xl shadow-xl transform transition-all duration-300 group-hover:scale-[1.02]"></div>
              <div className="relative p-3 text-white z-10 text-center">
                <h2 className="text-xl font-bold mb-1">Get In Touch</h2>
                <p className="text-sm mb-2">
                  We'd love to hear from you. Let's start a conversation.
                </p>
                <Link to="/contact" className="inline-block px-5 py-2 bg-white text-[#0d47a1] font-bold rounded-full hover:bg-opacity-90 transition-all duration-300 hover:scale-105 shadow-lg text-sm">
                  Contact Us
                </Link>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default AboutUs;
