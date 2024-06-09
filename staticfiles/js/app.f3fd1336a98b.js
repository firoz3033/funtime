 // sidebar sticky

 const contentArea = document.querySelector('.content-area')
 const sideBar = document.querySelector('.side-bar')
 
 // run function on load, scroll and resize for better performance
 window.onload = () => controlSideBarFloating()
 window.onscroll = () => controlSideBarFloating()
 window.onresize = () => controlSideBarFloating()
 
 // lets define some variables
 var leftBlock = contentArea
 var rightBlock = sideBar
 var topSpace = 10
 var breakpoint = 992  // we use 992 for col-lg
 var stickyClass = 'sticky-sidebar'
 var bottomFixedClass = 'bottom-fixed-sidebar'
 
 // now create a function that will create sticky sidebar and use above variables
 function controlSideBarFloating(){
     var rectL = leftBlock.getBoundingClientRect();
     var rectR = rightBlock.getBoundingClientRect();
     if(window.innerWidth >= breakpoint){
         if(rectL.top-topSpace + (rectL.height - rectR.height) >= 0 && rectL.top-topSpace <= 0){
             rightBlock.classList.add(stickyClass)
             rightBlock.classList.remove(bottomFixedClass)
         }else if(rectL.top-topSpace + (rectL.height - rectR.height) <= 0){
             rightBlock.classList.remove(stickyClass)
             rightBlock.classList.add(bottomFixedClass)
         }else{
             rightBlock.classList.remove(stickyClass)
             rightBlock.classList.remove(bottomFixedClass)
         }
     }else{
         rightBlock.classList.remove(stickyClass)
         rightBlock.classList.remove(bottomFixedClass)
     }
 }

//  types js 


var typed = new Typed('#typed', {
    strings: ['Web Development', 'Graphics Designing','Digital Marketing','Programming Languages','Seo'],
    typeSpeed: 100,
    loop: true,
    loopCount: Infinity,
  });



  // testimonial swiper 

  var swiper = new Swiper(".mySwiper", {
    slidesPerView: 1,
    spaceBetween: 30,
    autoplay: {
      delay: 2500,
      disableOnInteraction: false,
    },
    breakpoints:{
      769:{
        slidesPerView: 2,
        spaceBetween: 30,
      },
    },
    pagination: {
      el: ".swiper-pagination",
      clickable: true,
    },
  });


 



// for validat 
