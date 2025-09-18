// This file handles the core application logic, state management, and UI rendering.

document.addEventListener('DOMContentLoaded', () => {
    
    // --- STATE AND CONSTANTS --- //
    let isAnalyzing = false;
    let selectedFile = null;
    let previewUrl = null;
    
    // --- DOM ELEMENT REFERENCES --- //
    const chatbotContainer = document.getElementById('chatbot-container');
    const resultsContainer = document.getElementById('results-container');
    const aboutContainer = document.getElementById('about-container');
    const footerContainer = document.getElementById('footer-container');

    // --- CORE FUNCTIONS --- //

    /**
     * Displays a toast notification.
     * @param {object} {title, description, variant, duration}
     */
    const showToast = ({ title, description, variant, duration = 3000 }) => {
        const toastContainer = document.getElementById('toast-container');
        const toast = document.createElement('div');
        toast.className = `toast ${variant === 'destructive' ? 'bg-red-800 text-white' : ''}`;
        toast.innerHTML = `<h3 class="font-semibold">${title}</h3><p class="text-sm ${variant === 'destructive' ? 'text-gray-200' : 'text-gray-400'}">${description}</p>`;
        toastContainer.appendChild(toast);
        
        gsap.fromTo(toast, {x: '110%'}, {x: '0%', className: 'toast show', duration: 0.5, ease: 'power3.out'});
        setTimeout(() => {
            gsap.to(toast, {x: '110%', duration: 0.5, ease: 'power3.in', onComplete: () => toast.remove()});
        }, duration);
    };
    
    /**
     * Handles the file analysis process, including a simulated API call.
     * @param {File} file The image file to analyze.
     */
    const handleAnalyze = async (file) => {
        if (!file) return;
        isAnalyzing = true;
        renderChatBot();
        
        const simulateAnalysis = (file) => new Promise((resolve) => {
            setTimeout(() => {
                const isHealthy = Math.random() > 0.5;
                resolve(isHealthy
                    ? { prediction: 'Healthy', confidence: `${Math.floor(Math.random() * 8) + 92}%`, isDiseased: false, file }
                    : { prediction: 'Leaf Rust', confidence: `${Math.floor(Math.random() * 15) + 85}%`, isDiseased: true, file }
                );
            }, 3000);
        });

        try {
            const result = await simulateAnalysis(file);
            showToast({
                title: "Analysis Complete!",
                description: `Detection: ${result.prediction} (${result.confidence})`,
            });
            renderResults(result);
            setTimeout(() => {
                document.getElementById('results')?.scrollIntoView({ behavior: 'smooth' });
                ScrollTrigger.refresh();
                initializeScrollAnimations();
            }, 100);
        } catch (error) {
            console.error("Analysis Error:", error);
            showToast({ title: "Analysis Failed", description: "There was an error analyzing your image.", variant: "destructive" });
        } finally {
            isAnalyzing = false;
            renderChatBot();
        }
    };

    // --- UI RENDERING FUNCTIONS --- //

    /**
     * Renders the main chatbot/uploader interface.
     */
    const renderChatBot = () => {
         const analyzingUI = `
            <div class="mt-4 p-4 rounded-lg bg-gray-800/50 border border-gray-700/50">
                <div class="flex items-center gap-3">
                    <i data-lucide="loader-2" class="w-5 h-5 text-green-400 animate-spin"></i>
                    <div>
                        <p class="font-medium">Analyzing your plant...</p>
                        <p class="text-sm text-gray-400">Our AI is examining the image...</p>
                    </div>
                </div>
            </div>`;
        
        const imagePreviewUI = previewUrl ? `
            <div class="mb-4 p-3 border border-gray-700/50 rounded-lg bg-gray-900/30">
                <div class="flex items-center gap-3">
                    <img src="${previewUrl}" alt="Plant preview" class="w-12 h-12 rounded object-cover flex-shrink-0" />
                    <div class="flex-1 min-w-0">
                        <p class="text-sm font-medium text-green-400 truncate">${selectedFile?.name}</p>
                        <p class="text-xs text-gray-400">Ready for analysis</p>
                    </div>
                    <button id="remove-file-btn" type="button" class="text-xs px-2 py-1 rounded hover:bg-gray-700/50 btn-press">Remove</button>
                </div>
            </div>` : '';

        const cardPaddingClass = selectedFile ? 'p-8' : 'p-6';

        chatbotContainer.innerHTML = `
            <section class="relative min-h-screen flex items-end justify-center px-4 pb-20 overflow-hidden" id="uploader">
                <div class="relative z-10 w-full max-w-4xl mx-auto" id="hero-content-wrapper">
                    <div class="text-center mb-12 hero-anim-item">
                        <h1 class="text-5xl md:text-7xl font-bold mb-6 text-white">
                            AI Plant Disease
                            <span class="block gradient-nature bg-clip-text text-transparent">Detector</span>
                        </h1>
                        <p class="text-xl md:text-2xl text-gray-300 max-w-2xl mx-auto">
                            Upload a leaf image for instant disease detection
                        </p>
                    </div>
                    <div class="gradient-card border border-white/20 shadow-nature backdrop-blur-md rounded-lg hero-anim-item">
                        <div class="${cardPaddingClass} transition-all duration-300">
                            ${imagePreviewUI}
                            <form id="analysis-form" class="flex gap-3">
                                <input id="message-input" type="text" placeholder="Your image is ready to analyze..." class="flex-1 bg-gray-900/50 border border-gray-700/50 focus:border-green-500 rounded-md px-3 text-white" disabled value="Analyze this plant image">
                                <button type="submit" class="gradient-nature hover:shadow-glow transition-all duration-300 px-4 py-2 rounded-md btn-press" ${!selectedFile || isAnalyzing ? 'disabled' : ''}>
                                    ${isAnalyzing ? '<i data-lucide="loader-2" class="w-4 h-4 animate-spin"></i>' : '<i data-lucide="send" class="w-4 h-4"></i>'}
                                </button>
                            </form>
                            <div id="drop-zone" class="border-2 border-dashed border-gray-600 rounded-lg p-4 mt-4 text-center cursor-pointer hover:border-green-500/50 ${previewUrl ? 'hidden' : ''}">
                                <input type="file" id="file-input" accept="image/*" class="hidden" />
                                <div class="flex items-center justify-center gap-3 text-sm text-gray-400">
                                    <i data-lucide="upload-cloud" class="w-5 h-5 text-gray-500"></i>
                                    <span>Click, or drag and drop an image here</span>
                                </div>
                            </div>
                            ${isAnalyzing ? analyzingUI : ''}
                        </div>
                    </div>
                </div>
            </section>`;
        attachChatBotListeners();
        lucide.createIcons();
    };

    /**
     * Renders the analysis results section.
     * @param {object} result The analysis result object.
     */
    const renderResults = (result) => {
        if (!result) { resultsContainer.classList.add('hidden'); return; }
        const imageUrl = URL.createObjectURL(result.file);
        const isDiseased = result.isDiseased;
        
        resultsContainer.innerHTML = `
            <div id="results" class="py-20 px-4">
                <div class="max-w-4xl mx-auto anim-section">
                    <div class="text-center mb-12">
                        <h2 class="text-3xl md:text-4xl font-bold mb-4 text-white">Analysis Results</h2>
                        <p class="text-lg text-gray-400">Here's what our AI detected in your plant image</p>
                    </div>
                    <div class="grid md:grid-cols-2 gap-8 items-center">
                        <div class="gradient-card border border-white/10 shadow-nature overflow-hidden rounded-lg">
                            <img src="${imageUrl}" alt="Analyzed plant" class="w-full h-64 md:h-80 object-cover" />
                        </div>
                        <div class="gradient-card border border-white/10 shadow-nature rounded-lg p-6 space-y-4">
                            <div class="flex items-center gap-3">
                                <div class="p-2 rounded-full ${isDiseased ? 'bg-red-500/20' : 'bg-green-500/20'}">
                                    ${isDiseased ? '<i data-lucide="alert-triangle" class="w-6 h-6 text-diseased"></i>' : '<i data-lucide="check-circle" class="w-6 h-6 text-healthy"></i>'}
                                </div>
                                <span class="text-xl text-white">Diagnosis</span>
                            </div>
                            <div>
                                <h3 class="text-2xl font-bold ${isDiseased ? 'text-diseased' : 'text-healthy'}">${result.prediction}</h3>
                                <div class="flex items-center gap-2 mt-2">
                                    <span class="text-gray-400">Confidence:</span>
                                    <span class="border-2 px-2 py-0.5 rounded-full text-sm ${isDiseased ? 'border-diseased text-diseased' : 'border-healthy text-healthy'}">${result.confidence}</span>
                                </div>
                            </div>
                            <div class="p-4 rounded-lg bg-gray-900/30 border border-white/10">
                                <div class="flex items-start gap-3">
                                    <i data-lucide="leaf" class="w-5 h-5 text-green-400 mt-0.5"></i>
                                    <div class="space-y-2 text-sm">
                                        ${isDiseased 
                                            ? `<p class="font-medium text-red-400">Disease Detected</p><p class="text-gray-400">We've identified signs of ${result.prediction.toLowerCase()}. Consider consulting a specialist.</p>`
                                            : `<p class="font-medium text-green-400">Plant Looks Healthy!</p><p class="text-gray-400">Continue your current care routine and monitor regularly.</p>`
                                        }
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>`;
        resultsContainer.classList.remove('hidden');
        lucide.createIcons();
    };

    /**
     * Renders the "About" section.
     */
    const renderAboutSection = () => {
        const features = [
            { icon: 'brain', title: "AI-Powered Analysis", description: "Advanced machine learning models trained on thousands of plant disease images for accurate detection." },
            { icon: 'camera', title: "Simple Image Upload", description: "Just snap a photo or upload an image of your plant leaf for instant analysis." },
            { icon: 'zap', title: "Instant Results", description: "Get detailed health reports and disease identification in seconds, not days." },
            { icon: 'shield', title: "Trusted Diagnostics", description: "Our models are continuously updated with the latest research in plant pathology." }
        ];

        aboutContainer.innerHTML = `
            <section class="py-20 px-4" id="about">
                <div class="max-w-6xl mx-auto anim-section">
                    <div class="text-center mb-16">
                        <h2 class="text-3xl md:text-4xl font-bold mb-4 text-white">About Our AI Detector</h2>
                        <p class="text-lg text-gray-400 max-w-3xl mx-auto">Our technology uses computer vision to provide accurate plant disease detection.</p>
                    </div>
                    <div class="grid md:grid-cols-2 lg:grid-cols-4 gap-6">
                        ${features.map(f => `
                            <div class="gradient-card border border-white/10 shadow-nature hover:shadow-glow transition-all duration-300 hover:scale-105 rounded-lg p-6 text-center backdrop-blur-sm">
                                <div class="mx-auto gradient-nature p-3 rounded-full w-fit mb-4"><i data-lucide="${f.icon}" class="w-6 h-6 text-green-900"></i></div>
                                <h3 class="text-lg font-bold text-white mb-2">${f.title}</h3>
                                <p class="text-sm text-gray-400">${f.description}</p>
                            </div>`).join('')}
                    </div>
                </div>
            </section>`;
    };
    
    /**
     * Renders the footer.
     */
    const renderFooter = () => {
        footerContainer.innerHTML = `
            <div class="border-t border-white/20" style="background: hsl(120, 15%, 8%)">
                <div class="max-w-6xl mx-auto px-4 py-12 text-center text-sm text-gray-400">
                   <p>&copy; ${new Date().getFullYear()} AI Plant Disease Detector.</p>
                   <div class="flex justify-center gap-6 mt-4">
                        <a href="https://github.com" target="_blank" rel="noopener noreferrer" class="text-gray-400 hover:text-white transition-colors">
                            <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="currentColor" class="w-6 h-6"><path d="M12 0c-6.626 0-12 5.373-12 12 0 5.302 3.438 9.8 8.207 11.387.599.111.793-.261.793-.577v-2.234c-3.338.726-4.033-1.416-4.033-1.416-.546-1.387-1.333-1.756-1.333-1.756-1.089-.745.083-.729.083-.729 1.205.084 1.839 1.237 1.839 1.237 1.07 1.834 2.807 1.304 3.492.997.107-.775.418-1.305.762-1.604-2.665-.305-5.467-1.334-5.467-5.931 0-1.311.469-2.381 1.236-3.221-.124-.303-.535-1.524.117-3.176 0 0 1.008-.322 3.301 1.23.957-.266 1.983-.399 3.003-.404 1.02.005 2.047.138 3.006.404 2.291-1.552 3.297-1.23 3.297-1.23.653 1.653.242 2.874.118 3.176.77.84 1.235 1.91 1.235 3.221 0 4.609-2.807 5.624-5.479 5.921.43.372.823 1.102.823 2.222v3.293c0 .319.192.694.801.576 4.765-1.589 8.199-6.086 8.199-11.386 0-6.627-5.373-12-12-12z"/></svg>
                        </a>
                        <a href="https://linkedin.com" target="_blank" rel="noopener noreferrer" class="text-gray-400 hover:text-white transition-colors">
                           <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="currentColor" class="w-6 h-6"><path d="M4.98 3.5c0 1.381-1.11 2.5-2.48 2.5s-2.48-1.119-2.48-2.5c0-1.38 1.11-2.5 2.48-2.5s2.48 1.12 2.48 2.5zm.02 4.5h-5v16h5v-16zm7.982 0h-4.968v16h4.969v-8.399c0-4.67 6.029-4.499 6.029 0v8.399h4.988v-10.131c0-7.88-8.922-7.59-11.018-3.714v-2.155z"/></svg>
                        </a>
                   </div>
                </div>
            </div>`;
    };

    /**
     * Attaches event listeners to the chatbot/uploader form.
     */
    const attachChatBotListeners = () => {
        const form = document.getElementById('analysis-form');
        const dropZone = document.getElementById('drop-zone');
        const fileInput = document.getElementById('file-input');
        const removeFileBtn = document.getElementById('remove-file-btn');
        
        const handleFileSelect = (file) => {
            if (file?.type.startsWith('image/')) {
                selectedFile = file;
                previewUrl = URL.createObjectURL(file);
                renderChatBot();
            } else if (file) {
                showToast({ title: "Invalid File", description: "Please upload a valid image file.", variant: "destructive" });
            }
        };

        if(form) {
            form.onsubmit = (e) => { e.preventDefault(); if (selectedFile && !isAnalyzing) handleAnalyze(selectedFile); };
        }

        if (removeFileBtn) { 
            removeFileBtn.onclick = () => { 
                selectedFile = null; 
                if (previewUrl) URL.revokeObjectURL(previewUrl); 
                previewUrl = null; 
                renderChatBot(); 
            }; 
        }

        if (dropZone) {
            dropZone.onclick = () => fileInput.click();
            dropZone.ondragover = (e) => { e.preventDefault(); dropZone.classList.add('border-green-500', 'bg-green-500/10'); };
            dropZone.ondragleave = (e) => { e.preventDefault(); dropZone.classList.remove('border-green-500', 'bg-green-500/10'); };
            dropZone.ondrop = (e) => { 
                e.preventDefault(); 
                dropZone.classList.remove('border-green-500', 'bg-green-500/10'); 
                handleFileSelect(e.dataTransfer.files[0]); 
            };
        }

        if(fileInput) {
            fileInput.onchange = (e) => handleFileSelect(e.target.files[0]);
        }
    };

    // --- APP INITIALIZATION --- //

    /**
     * Initializes the entire application on page load.
     */
    const initializeApp = () => {
        // Render initial UI components
        renderChatBot();
        renderAboutSection();
        renderFooter();
        lucide.createIcons();

        // Run the loader animation and set up scroll animations as a callback
        runLoaderAnimation(initializeScrollAnimations);
    };

    initializeApp();
});