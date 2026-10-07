/* ==========================================================================
   SHAIK HARUN PORTFOLIO - 4K CINEMATIC JAVASCRIPT ENGINE
   Includes: Live Background Particle Canvas, 3D Card Tilt, Typewriter, Scroll-Spy, Modal
   ========================================================================== */

document.addEventListener('DOMContentLoaded', () => {
    
    /* ----------------------------------------------------------------------
       1. 4K LIVE INTERACTIVE BACKGROUND CANVAS (NEON PARTICLES)
       ---------------------------------------------------------------------- */
    const canvas = document.getElementById('cinematic-canvas');
    if (canvas) {
        const ctx = canvas.getContext('2d');
        let width = canvas.width = window.innerWidth;
        let height = canvas.height = window.innerHeight;

        window.addEventListener('resize', () => {
            width = canvas.width = window.innerWidth;
            height = canvas.height = window.innerHeight;
        }, { passive: true });

        const particles = [];
        const particleCount = Math.min(Math.floor(width * 0.04), 65);

        class Particle {
            constructor() {
                this.reset();
            }

            reset() {
                this.x = Math.random() * width;
                this.y = Math.random() * height;
                this.vx = (Math.random() - 0.5) * 0.4;
                this.vy = (Math.random() - 0.5) * 0.4;
                this.radius = Math.random() * 2 + 1;
                this.alpha = Math.random() * 0.5 + 0.2;
                this.color = Math.random() > 0.3 ? '#7c5cff' : '#a78bfa';
            }

            update() {
                this.x += this.vx;
                this.y += this.vy;

                if (this.x < 0 || this.x > width) this.vx *= -1;
                if (this.y < 0 || this.y > height) this.vy *= -1;
            }

            draw() {
                ctx.beginPath();
                ctx.arc(this.x, this.y, this.radius, 0, Math.PI * 2);
                ctx.fillStyle = this.color;
                ctx.globalAlpha = this.alpha;
                ctx.shadowBlur = 10;
                ctx.shadowColor = this.color;
                ctx.fill();
            }
        }

        for (let i = 0; i < particleCount; i++) {
            particles.push(new Particle());
        }

        function drawConnections() {
            for (let i = 0; i < particles.length; i++) {
                for (let j = i + 1; j < particles.length; j++) {
                    const dx = particles[i].x - particles[j].x;
                    const dy = particles[i].y - particles[j].y;
                    const dist = Math.sqrt(dx * dx + dy * dy);

                    if (dist < 130) {
                        ctx.beginPath();
                        ctx.moveTo(particles[i].x, particles[i].y);
                        ctx.lineTo(particles[j].x, particles[j].y);
                        ctx.strokeStyle = '#7c5cff';
                        ctx.globalAlpha = (1 - dist / 130) * 0.18;
                        ctx.lineWidth = 0.8;
                        ctx.stroke();
                    }
                }
            }
        }

        function animateCanvas() {
            ctx.clearRect(0, 0, width, height);
            
            particles.forEach(p => {
                p.update();
                p.draw();
            });

            drawConnections();
            requestAnimationFrame(animateCanvas);
        }

        requestAnimationFrame(animateCanvas);
    }

    /* ----------------------------------------------------------------------
       2. CUSTOM LAGGY GLOWING CURSOR (DESKTOP ONLY)
       ---------------------------------------------------------------------- */
    const cursorDot = document.getElementById('cursor-dot');
    const cursorHalo = document.getElementById('cursor-halo');

    let mouseX = window.innerWidth / 2;
    let mouseY = window.innerHeight / 2;
    let dotX = mouseX, dotY = mouseY;
    let haloX = mouseX, haloY = mouseY;

    const isTouchDevice = 'ontouchstart' in window || navigator.maxTouchPoints > 0;

    if (cursorDot && cursorHalo && !isTouchDevice) {
        window.addEventListener('mousemove', (e) => {
            mouseX = e.clientX;
            mouseY = e.clientY;
        }, { passive: true });

        function animateCursor() {
            dotX += (mouseX - dotX) * 0.25;
            dotY += (mouseY - dotY) * 0.25;

            haloX += (mouseX - haloX) * 0.12;
            haloY += (mouseY - haloY) * 0.12;

            cursorDot.style.transform = `translate3d(${dotX}px, ${dotY}px, 0) translate(-50%, -50%)`;
            cursorHalo.style.transform = `translate3d(${haloX}px, ${haloY}px, 0) translate(-50%, -50%)`;

            requestAnimationFrame(animateCursor);
        }
        requestAnimationFrame(animateCursor);

        // Hover effect for interactive elements
        const interactiveSelectors = 'a, button, .tilt-card, .portrait-halo-wrapper, .about-social-icon, .testimonial-card';
        document.querySelectorAll(interactiveSelectors).forEach((el) => {
            el.addEventListener('mouseenter', () => document.body.classList.add('hovering-interactive'));
            el.addEventListener('mouseleave', () => document.body.classList.remove('hovering-interactive'));
        });
    }

    /* ----------------------------------------------------------------------
       3. 3D CARD TILT PERSPECTIVE ANIMATION
       ---------------------------------------------------------------------- */
    const tiltCards = document.querySelectorAll('.tilt-card');
    if (!isTouchDevice) {
        tiltCards.forEach(card => {
            card.addEventListener('mousemove', (e) => {
                const rect = card.getBoundingClientRect();
                const x = e.clientX - rect.left;
                const y = e.clientY - rect.top;

                const centerX = rect.width / 2;
                const centerY = rect.height / 2;

                const rotateX = ((y - centerY) / centerY) * -8;
                const rotateY = ((x - centerX) / centerX) * 8;

                card.style.transform = `perspective(1000px) rotateX(${rotateX}deg) rotateY(${rotateY}deg) translateY(-4px)`;
            });

            card.addEventListener('mouseleave', () => {
                card.style.transform = `perspective(1000px) rotateX(0deg) rotateY(0deg) translateY(0px)`;
            });
        });
    }

    /* ----------------------------------------------------------------------
       4. TYPEWRITER EFFECT (STATIONARY IN-PLACE + UNIQUE COLOR PER TITLE)
       ---------------------------------------------------------------------- */
    const typewriterElement = document.getElementById('typewriter-text');
    if (typewriterElement) {
        const roleObjects = [
            { title: 'Web Developer', color: 'linear-gradient(135deg, #e9d5ff 0%, #c084fc 50%, #a855f7 100%)' },
            { title: 'Software Engineer', color: 'linear-gradient(135deg, #bae6fd 0%, #38bdf8 50%, #0284c7 100%)' },
            { title: 'Python Developer', color: 'linear-gradient(135deg, #bbf7d0 0%, #4ade80 50%, #facc15 100%)' },
            { title: 'Backend Developer', color: 'linear-gradient(135deg, #fef08a 0%, #fb923c 50%, #f43f5e 100%)' },
            { title: 'Prompt Engineer', color: 'linear-gradient(135deg, #fbcfe8 0%, #f472b6 50%, #ec4899 100%)' },
            { title: 'Vibe Coder', color: 'linear-gradient(135deg, #fde047 0%, #f97316 50%, #a855f7 100%)' }
        ];

        let roleIndex = 0;
        let charIndex = 0;
        let isDeleting = false;

        function typeLoop() {
            const currentItem = roleObjects[roleIndex];
            const currentTitle = currentItem.title;

            // Apply unique background gradient per title
            typewriterElement.style.backgroundImage = currentItem.color;

            if (isDeleting) {
                typewriterElement.textContent = currentTitle.substring(0, charIndex--);
            } else {
                typewriterElement.textContent = currentTitle.substring(0, charIndex++);
            }

            let typeSpeed = isDeleting ? 40 : (65 + Math.random() * 35);

            if (!isDeleting && charIndex > currentTitle.length) {
                typeSpeed = 2200; // Hold title for 2.2 seconds
                isDeleting = true;
            } else if (isDeleting && charIndex < 0) {
                isDeleting = false;
                roleIndex = (roleIndex + 1) % roleObjects.length;
                charIndex = 0;
                typeSpeed = 350; // Pause before next title
            }

            setTimeout(typeLoop, typeSpeed);
        }

        typewriterElement.textContent = '';
        setTimeout(typeLoop, 400);
    }

    /* ----------------------------------------------------------------------
       5. NAVBAR SCROLL EFFECT & MOBILE NAVIGATION DRAWER
       ---------------------------------------------------------------------- */
    const navbar = document.getElementById('navbar');
    const navToggle = document.getElementById('nav-toggle');
    const navLinks = document.getElementById('nav-links');
    const navOverlay = document.getElementById('nav-overlay');

    window.addEventListener('scroll', () => {
        if (window.scrollY > 40) {
            navbar.classList.add('scrolled');
        } else {
            navbar.classList.remove('scrolled');
        }
    }, { passive: true });

    function toggleMobileMenu() {
        if (!navToggle || !navLinks) return;
        const isOpen = navLinks.classList.contains('mobile-open');
        
        if (isOpen) {
            navToggle.classList.remove('open');
            navLinks.classList.remove('mobile-open');
            if (navOverlay) navOverlay.classList.remove('active');
            document.body.style.overflow = '';
        } else {
            navToggle.classList.add('open');
            navLinks.classList.add('mobile-open');
            if (navOverlay) navOverlay.classList.add('active');
            document.body.style.overflow = 'hidden';
        }
    }

    if (navToggle) navToggle.addEventListener('click', toggleMobileMenu);
    if (navOverlay) navOverlay.addEventListener('click', toggleMobileMenu);

    document.querySelectorAll('.nav-link').forEach(link => {
        link.addEventListener('click', () => {
            if (navLinks && navLinks.classList.contains('mobile-open')) {
                toggleMobileMenu();
            }
        });
    });

    /* ----------------------------------------------------------------------
       6. SCROLL-SPY USING INTERSECTIONOBSERVER
       ---------------------------------------------------------------------- */
    const sections = document.querySelectorAll('section');
    const navItems = document.querySelectorAll('.nav-link');

    const observerOptions = {
        threshold: 0.25,
        rootMargin: '-50px 0px -20% 0px'
    };

    const scrollSpyObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const id = entry.target.getAttribute('id');
                navItems.forEach(item => {
                    if (item.getAttribute('href') === `#${id}`) {
                        item.classList.add('active');
                    } else {
                        item.classList.remove('active');
                    }
                });
            }
        });
    }, observerOptions);

    sections.forEach(section => scrollSpyObserver.observe(section));

    /* ----------------------------------------------------------------------
       7. SCROLL REVEAL ANIMATION
       ---------------------------------------------------------------------- */
    const revealElements = document.querySelectorAll('.scroll-reveal');
    const revealObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('revealed');
                revealObserver.unobserve(entry.target);
            }
        });
    }, { threshold: 0.1 });

    revealElements.forEach(el => revealObserver.observe(el));

    /* ----------------------------------------------------------------------
       8. WORK EXPERIENCE / EDUCATION TIMELINE TOGGLE
       ---------------------------------------------------------------------- */
    const tabExperience = document.getElementById('tab-experience');
    const tabEducation = document.getElementById('tab-education');
    const toggleSlider = document.getElementById('toggle-slider');
    const timelineItems = document.getElementById('timeline-items');

    const experienceData = [
        {
            title: "Python Full Stack Training",
            org: "Pentagon Space",
            date: "May 2024 – Dec 2024",
            desc: "Completed 300+ hour full-stack program in Python, Django, JavaScript, and REST APIs; used NumPy and Pandas to clean, analyze, and visualize 5+ datasets in Matplotlib and Excel."
        },
        {
            title: "AWS Cloud Intern",
            org: "BrainOvision Solutions Pvt. Ltd",
            date: "Jan 2023 – Apr 2023",
            desc: "Gained knowledge on the basics of cloud infrastructure, deployment, and resource management through hands-on EC2 practice."
        },
        {
            title: "Software Engineering Virtual Intern",
            org: "J.P. Morgan Chase & Co. (via Forage)",
            date: "Virtual Program",
            desc: "Gained hands-on experience with stock price data, data visualization, including an open-source contribution."
        }
    ];

    const educationData = [
        {
            title: "Bachelor of Technology in CS & Engineering",
            org: "Annamacharya Institute of Technology and Sciences, Kadapa",
            date: "Oct 2020 – Jan 2025",
            desc: "Graduated with 7.4 CGPA. Specialized in Full-Stack Web Development, Data Structures & Algorithms, System Design, and Database Management."
        },
        {
            title: "Intermediate (MPC)",
            org: "Narayana Junior College",
            date: "Sept 2018 – Mar 2020",
            desc: "Graduated with 8.6 CGPA. Rigorous coursework in Higher Mathematics, Physics, and Physical Sciences."
        },
        {
            title: "Secondary Education (SSC)",
            org: "Sarada High School",
            date: "Jan 2017 – Feb 2018",
            desc: "Graduated with 8.8 CGPA. Recognized for academic excellence and foundational problem-solving."
        }
    ];

    function renderTimeline(data) {
        if (!timelineItems) return;
        timelineItems.style.opacity = '0';
        timelineItems.style.transform = 'translateY(15px)';
        
        setTimeout(() => {
            timelineItems.innerHTML = data.map(item => `
                <div class="timeline-item">
                    <div class="timeline-dot"></div>
                    <div class="timeline-content-card tilt-card">
                        <div class="timeline-header-group">
                            <div>
                                <h3 class="timeline-title">${item.title}</h3>
                                <span class="timeline-org">${item.org}</span>
                            </div>
                            <div class="timeline-date">${item.date}</div>
                        </div>
                        <p class="timeline-desc">${item.desc}</p>
                    </div>
                </div>
            `).join('');

            timelineItems.style.opacity = '1';
            timelineItems.style.transform = 'translateY(0)';
        }, 200);
    }

    if (tabExperience && tabEducation && toggleSlider) {
        tabExperience.addEventListener('click', () => {
            tabExperience.classList.add('active');
            tabEducation.classList.remove('active');
            toggleSlider.classList.remove('slide-right');
            renderTimeline(experienceData);
        });

        tabEducation.addEventListener('click', () => {
            tabEducation.classList.add('active');
            tabExperience.classList.remove('active');
            toggleSlider.classList.add('slide-right');
            renderTimeline(educationData);
        });
    }

    /* ----------------------------------------------------------------------
       9. DYNAMIC INFINITE TESTIMONIALS MARQUEE
       ---------------------------------------------------------------------- */
    const testimonialsTrack = document.getElementById('testimonials-track');
    if (testimonialsTrack) {
        const originalCards = Array.from(testimonialsTrack.children);
        originalCards.forEach(card => {
            const clone = card.cloneNode(true);
            testimonialsTrack.appendChild(clone);
        });
    }

    /* ----------------------------------------------------------------------
       10. COPY EMAIL TO CLIPBOARD WITH TOAST
       ---------------------------------------------------------------------- */
    const copyEmailBtn = document.getElementById('copy-email-btn');
    const toast = document.getElementById('toast');

    if (copyEmailBtn && toast) {
        copyEmailBtn.addEventListener('click', () => {
            const email = "shaikharun811@gmail.com";
            navigator.clipboard.writeText(email).then(() => {
                toast.classList.add('show');
                setTimeout(() => {
                    toast.classList.remove('show');
                }, 3200);
            }).catch(err => {
                console.error("Could not copy email: ", err);
            });
        });
    }

    /* ----------------------------------------------------------------------
       11. RESUME MODAL HANDLER
       ---------------------------------------------------------------------- */
    const resumeModal = document.getElementById('resume-modal');
    const resumeBackdrop = document.getElementById('resume-backdrop');
    const closeResumeModal = document.getElementById('close-resume-modal');
    const resumeTriggers = document.querySelectorAll('.open-resume-trigger, #floating-resume-btn');

    function openModal() {
        if (resumeModal) {
            resumeModal.classList.add('active');
            document.body.style.overflow = 'hidden';
        }
    }

    function closeModal() {
        if (resumeModal) {
            resumeModal.classList.remove('active');
            document.body.style.overflow = '';
        }
    }

    resumeTriggers.forEach(btn => btn.addEventListener('click', openModal));
    if (closeResumeModal) closeResumeModal.addEventListener('click', closeModal);
    if (resumeBackdrop) resumeBackdrop.addEventListener('click', closeModal);

    document.addEventListener('keydown', (e) => {
        if (e.key === 'Escape' && resumeModal && resumeModal.classList.contains('active')) {
            closeModal();
        }
    });

    /* ----------------------------------------------------------------------
       12. 100% GUARANTEED LOCALHOST & BROWSER AI AUDIO PLAYBACK ENGINE
       ---------------------------------------------------------------------- */
    const welcomeAudio = document.getElementById('welcome-audio');
    const aiAudioBanner = document.getElementById('ai-audio-banner');
    const aiAudioBannerText = document.getElementById('ai-audio-banner-text');
    let hasPlayedAudio = false;
    let audioContext = null;

    function showAudioBanner(msg, duration = 6500) {
        if (!aiAudioBanner) return;
        if (aiAudioBannerText) aiAudioBannerText.textContent = msg;
        aiAudioBanner.classList.add('show');

        if (duration > 0) {
            setTimeout(() => {
                aiAudioBanner.classList.remove('show');
            }, duration);
        }
    }

    function forcePlayOnLocalhost() {
        if (hasPlayedAudio) return;

        if (welcomeAudio) {
            welcomeAudio.currentTime = 0;
            welcomeAudio.volume = 1.0;

            const promise = welcomeAudio.play();
            if (promise !== undefined) {
                promise.then(() => {
                    hasPlayedAudio = true;
                    showAudioBanner('🔊 AI Voice Greeting Playing...');
                    console.log('✅ HTML5 Audio welcome.wav playing on localhost.');
                }).catch(err => {
                    console.warn('⚠️ Chrome Autoplay policy held cold start. Unlocking via Web Audio API & ambient viewport movement:', err);
                    unlockWebAudioContext();
                });
            }
        } else {
            unlockWebAudioContext();
        }
    }

    function unlockWebAudioContext() {
        if (hasPlayedAudio) return;
        try {
            const AudioCtxClass = window.AudioContext || window.webkitAudioContext;
            if (AudioCtxClass) {
                if (!audioContext) audioContext = new AudioCtxClass();
                if (audioContext.state === 'suspended') {
                    audioContext.resume();
                }

                fetch('assets/audio/welcome.mp3')
                    .then(res => res.arrayBuffer())
                    .then(buffer => audioContext.decodeAudioData(buffer))
                    .then(audioBuffer => {
                        if (hasPlayedAudio) return;
                        const source = audioContext.createBufferSource();
                        const gainNode = audioContext.createGain();
                        gainNode.gain.value = 2.0;
                        source.buffer = audioBuffer;
                        source.connect(gainNode);
                        gainNode.connect(audioContext.destination);
                        source.start(0);
                        hasPlayedAudio = true;
                        showAudioBanner('🔊 AI Voice Greeting Playing...');
                        console.log('✅ Web Audio API welcome.mp3 playing successfully.');
                    })
                    .catch(err => {
                        console.warn('Web Audio buffer error, attempting welcome.wav:', err);
                        fetch('assets/audio/welcome.wav')
                            .then(res => res.arrayBuffer())
                            .then(buffer => audioContext.decodeAudioData(buffer))
                            .then(audioBuffer => {
                                if (hasPlayedAudio) return;
                                const source = audioContext.createBufferSource();
                                const gainNode = audioContext.createGain();
                                gainNode.gain.value = 2.0;
                                source.buffer = audioBuffer;
                                source.connect(gainNode);
                                gainNode.connect(audioContext.destination);
                                source.start(0);
                                hasPlayedAudio = true;
                                showAudioBanner('🔊 AI Voice Greeting Playing...');
                            })
                            .catch(e => playSpeechFallback());
                    });
            } else {
                playSpeechFallback();
            }
        } catch (e) {
            playSpeechFallback();
        }
    }

    function playSpeechFallback() {
        if (hasPlayedAudio || !('speechSynthesis' in window)) return;
        try {
            window.speechSynthesis.cancel();
            const text = "Hey there. Welcome to my world, A mind full of ideas, a screen full of possibilities, and a passion for making them real.";
            const utterance = new SpeechSynthesisUtterance(text);
            utterance.rate = 0.95;
            utterance.pitch = 1.05;
            utterance.volume = 1.0;
            
            utterance.onstart = () => {
                hasPlayedAudio = true;
                showAudioBanner('🔊 AI Voice Greeting Playing...');
            };

            const voices = window.speechSynthesis.getVoices();
            const aiVoice = voices.find(v => (v.name.includes('Google') || v.name.includes('Natural') || v.name.includes('Microsoft')) && v.lang.startsWith('en')) || voices.find(v => v.lang.startsWith('en'));
            if (aiVoice) utterance.voice = aiVoice;

            window.speechSynthesis.speak(utterance);
        } catch (e) {
            console.warn('SpeechSynthesis error:', e);
        }
    }

    // Immediate load triggers
    forcePlayOnLocalhost();
    window.addEventListener('load', forcePlayOnLocalhost);
    window.addEventListener('pageshow', forcePlayOnLocalhost);
    document.addEventListener('DOMContentLoaded', forcePlayOnLocalhost);

    // Global viewport event triggers for Chrome Autoplay unlock
    const unlockEvents = ['mousemove', 'pointermove', 'scroll', 'touchstart', 'click', 'keydown', 'focus', 'mouseover', 'mouseenter', 'wheel'];

    function handleGlobalUnlock() {
        if (!hasPlayedAudio) {
            forcePlayOnLocalhost();
        }
        if (hasPlayedAudio) {
            if (aiAudioBanner) {
                showAudioBanner('🔊 AI Voice Greeting Playing...', 6500);
            }
            unlockEvents.forEach(evt => window.removeEventListener(evt, handleGlobalUnlock));
        }
    }

    unlockEvents.forEach(evt => {
        window.addEventListener(evt, handleGlobalUnlock, { passive: true });
    });

    // HTML5 Video Autoplay Helper
    function initWebVideos() {
        const videos = document.querySelectorAll('video');
        videos.forEach(video => {
            video.muted = true;
            video.playsInline = true;
            const playPromise = video.play();
            if (playPromise !== undefined) {
                playPromise.catch(err => {
                    const playOnUserAction = () => {
                        video.play();
                        ['touchstart', 'click', 'scroll', 'mousemove'].forEach(evt => {
                            window.removeEventListener(evt, playOnUserAction);
                        });
                    };
                    ['touchstart', 'click', 'scroll', 'mousemove'].forEach(evt => {
                        window.addEventListener(evt, playOnUserAction, { passive: true });
                    });
                });
            }
        });
    }
    initWebVideos();
    window.addEventListener('load', initWebVideos);

});
