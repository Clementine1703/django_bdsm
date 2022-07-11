document.addEventListener('DOMContentLoaded', function(){
	let blocks = document.querySelectorAll('.carousel-inner');
	let indicators = document.querySelectorAll('.carousel-indicators');

	indicators.forEach(function(el){
	    console.log(el.querySelector('button'));
	    el.querySelector('button').setAttribute('aria-current', 'True');
		el.querySelector('button').classList.add('active');
	});
	blocks.forEach(function(item){
	    console.log(item.querySelector('.carousel-item'));
		item.querySelector('.carousel-item').classList.add('active');
	});

});