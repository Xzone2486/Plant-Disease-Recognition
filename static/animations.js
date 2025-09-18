// This file handles all GSAP animations for the application.

/**
 * Initializes and runs the main loading animation.
 * @param {Function} onCompleteCallback - A function to call after the animation completes.
 */
function runLoaderAnimation(onCompleteCallback) {
    gsap.registerPlugin(ScrollTrigger);

    const masterTl = gsap.timeline({
        onComplete: onCompleteCallback,
    });
    
    // Radar pulse animation for the loader
    const radarTl = gsap.timeline({ repeat: -1 });
    radarTl.fromTo(".radar-ring", 
        { scale: 0, autoAlpha: 0.5 },
        { scale: 1, autoAlpha: 0, duration: 1.5, stagger: 0.3, ease: "power2.out" }
    );
    
    // Setting initial states for the leaf SVG
    gsap.set("#loader-leaf", { autoAlpha: 1 });
    gsap.set(".stem-group", { scaleY: 0, transformOrigin: "bottom center" });
    gsap.set(".leaf-left", { xPercent: -100, autoAlpha: 0 });
    gsap.set(".leaf-right", { xPercent: 100, autoAlpha: 0 });

    // Main loader animation sequence
    masterTl.to(".stem-group", { scaleY: 1, duration: 1.2, ease: "power2.out" })
            .to([".leaf-left", ".leaf-right"], { xPercent: 0, autoAlpha: 1, duration: 1.0, ease: "power2.out" }, "-=0.4")
            .to("#loader-leaf", { rotationY: 360, duration: 1.2, ease: "power2.inOut", transformOrigin: "center center" }, "+=0.1")
            .to(['#loader-leaf', '.radar-ring'], { autoAlpha: 0, duration: 0.5, ease: "power2.in" })
            .to('#loader-circle', { scale: 30, duration: 1.2, ease: 'expo.inOut' }, "<")
            .to('#loader', { autoAlpha: 0, duration: 0.75, onComplete: () => document.getElementById('loader').remove() }, "-=0.6")
            .to('#main-content', { opacity: 1, duration: 0.1 }, "<")
            .from('#hero-content-wrapper', { scaleX: 0, autoAlpha: 0, duration: 1, ease: 'power3.out', transformOrigin: 'center center' }, "-=0.5")
            .from('.hero-anim-item', { y: 30, autoAlpha: 0, duration: 0.8, stagger: 0.2, ease: 'power3.out' }, "-=0.6");
}

/**
 * Initializes scroll-triggered animations for sections.
 * This can be re-run to catch new sections added to the DOM (like the results).
 */
function initializeScrollAnimations() {
     gsap.utils.toArray('.anim-section').forEach(section => {
        if (!section.classList.contains('animated-scroll')) {
            section.classList.add('animated-scroll');
            gsap.from(section, {
                y: 50, 
                autoAlpha: 0, 
                duration: 1, 
                ease: 'power3.out',
                scrollTrigger: { 
                    trigger: section, 
                    start: 'top 80%', 
                    once: true 
                }
            });
        }
    });
}