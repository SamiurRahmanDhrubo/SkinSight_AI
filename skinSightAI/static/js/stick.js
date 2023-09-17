const primaryHeader = document.querySelector('.sticky') 
const scrollWatcher = document.createElement('.content');

scrollwatcher.setAttribute('data-scroll-watcher', '');
primaryHeader.before(scrollWatcher);
const navObserver = new IntersectionObserver((entries) => { 
    primaryHeader.classList.toggle('sticking', !entries[0].isIntersecting) 
}, {rootMargin: "500px 0px 0px 0px"});

navObserver.observe(scrollWatcher)