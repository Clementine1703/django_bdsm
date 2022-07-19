document.addEventListener( 'DOMContentLoaded' ,function() {

			$('#navbarNavDropdown').on('hide.bs.collapse', function () {
				document.querySelector('.burger').classList.remove('active');
			 })

			 $('#navbarNavDropdown').on('show.bs.collapse', function () {
				document.querySelector('.burger').classList.add('active');
			 })
		});