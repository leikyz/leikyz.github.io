/**
 * Media Gallery — multi-video player for project detail pages.
 * 
 * Usage in HTML:
 *
 *   <div class="media-gallery" data-count="3">
 *     <!-- Navigation arrows (hidden when 1 item via CSS) -->
 *     <button class="media-gallery-prev" aria-label="Previous">‹</button>
 *     <button class="media-gallery-next" aria-label="Next">›</button>
 *
 *     <!-- Main viewport: one .media-gallery-slot per video -->
 *     <div class="media-gallery-viewport">
 *       <div class="media-gallery-slot active" data-index="0">
 *         <span class="media-gallery-slot-label">Feature Name</span>
 *         <video src="../assets/videos/feature1.mp4" controls muted loop playsinline
 *                poster="../assets/images/projects/thumb1.png"></video>
 *       </div>
 *       <div class="media-gallery-slot" data-index="1">
 *         <span class="media-gallery-slot-label">Second Feature</span>
 *         <video src="../assets/videos/feature2.mp4" controls muted loop playsinline
 *                poster="../assets/images/projects/thumb2.png"></video>
 *       </div>
 *       <!-- ...more slots... -->
 *     </div>
 *
 *     <!-- Thumbnail strip -->
 *     <div class="media-gallery-strip">
 *       <div class="media-gallery-strip-inner">
 *         <button class="media-gallery-tab active" data-index="0">
 *           <div class="media-gallery-tab-thumb">
 *             <img src="../assets/images/projects/thumb1.png" alt="Feature Name">
 *           </div>
 *           <span class="media-gallery-tab-num">01</span>
 *           <span class="media-gallery-tab-name">Feature Name</span>
 *         </button>
 *         <button class="media-gallery-tab" data-index="1">
 *           <div class="media-gallery-tab-thumb">
 *             <img src="../assets/images/projects/thumb2.png" alt="Second Feature">
 *           </div>
 *           <span class="media-gallery-tab-num">02</span>
 *           <span class="media-gallery-tab-name">Second Feature</span>
 *         </button>
 *         <!-- ...more tabs... -->
 *       </div>
 *     </div>
 *   </div>
 *
 * Adding a video:
 *   1. Add a new <div class="media-gallery-slot"> in the viewport.
 *   2. Add a matching <button class="media-gallery-tab"> in the strip.
 *   3. Increment data-count="N" on the .media-gallery wrapper.
 *   JS picks up the rest automatically.
 */
(function () {
  'use strict';

  function initGallery(gallery) {
    const slots = gallery.querySelectorAll('.media-gallery-slot');
    const tabs  = gallery.querySelectorAll('.media-gallery-tab');
    const prev  = gallery.querySelector('.media-gallery-prev');
    const next  = gallery.querySelector('.media-gallery-next');

    if (!slots.length) return;

    let current = 0;

    function goTo(index, fromUser) {
      if (index < 0) index = slots.length - 1;
      if (index >= slots.length) index = 0;

      // Pause/stop the currently active video to avoid audio bleed
      const activeSlot = gallery.querySelector('.media-gallery-slot.active');
      if (activeSlot) {
        const vid = activeSlot.querySelector('video');
        if (vid) { vid.pause(); vid.currentTime = 0; }
      }

      // Swap active on slots
      slots.forEach((s, i) => s.classList.toggle('active', i === index));
      tabs.forEach((t, i)  => t.classList.toggle('active', i === index));

      // Scroll the active tab into view in the strip
      if (tabs[index]) {
        tabs[index].scrollIntoView({ behavior: 'smooth', block: 'nearest', inline: 'nearest' });
      }

      // Auto-play the new active video if switched by user interaction
      if (fromUser) {
        const newVid = slots[index] && slots[index].querySelector('video');
        if (newVid) {
          newVid.play().catch(() => {}); // ignore auto-play errors
        }
      }

      current = index;
    }

    // Tab clicks
    tabs.forEach((tab, i) => {
      tab.addEventListener('click', () => goTo(i, true));
    });

    // Arrow buttons
    if (prev) prev.addEventListener('click', () => goTo(current - 1, true));
    if (next) next.addEventListener('click', () => goTo(current + 1, true));

    // Keyboard arrow navigation when focus is inside the gallery
    gallery.addEventListener('keydown', (e) => {
      if (e.key === 'ArrowRight') { goTo(current + 1, true); e.preventDefault(); }
      if (e.key === 'ArrowLeft')  { goTo(current - 1, true); e.preventDefault(); }
    });
  }

  document.addEventListener('DOMContentLoaded', () => {
    document.querySelectorAll('.media-gallery').forEach(initGallery);
  });
})();
