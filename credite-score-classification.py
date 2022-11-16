import streamlit as st
import streamlit.components.v1 as com
with open("main.css") as source
  design = source.read()
com.html(f"""
											<!-- my Clinic -->
<div class="bottom_border">
<div class="container">
	<div class="sixteen columns top_1 ">
		<div class="twelve columns alpha " >
			<span class="logo1_font">Cek Layak Pinjam</span><span class="point_font">.</span><br>
			<span class="logo2_font">Buat Finansialmu Aman</span>	
		</div>
	<div class="four columns omega" >
		<span class="blockquote">

            		
        <span class="social_span">

          <li><a href="indexprofil.html"> Tentang Developer </a></li>
            
		</span>


	</div>
	</div>
</div>
 </div>
<div class="clearfix"></div>

										<!--Welcome to our High Quality -->
<div class="main_bg" data-stellar-background-ratio="0.5" >
<div class="container top_2">
	<div class="sixteen colmns">
		<div class="nine columns  alpha" >
			<span class="welcome_font">Selamat Datang Sahabat Uang! Kami Siap Membantu Urusan Finansial Anda</span><span class="point_font">.</span> 
			<div class="clearfix top_3"></div>
			<span class="text1_font">Kami Akan Membantu Anda, Jika Anda Sesuai Dengan Standart Yang Telah Di Tentukan Oleh Tim Kami, Jadi Segera Cek Kelayakan Anda, Dan Bantuan Akan Segera Datang.</span>
			<div class="clearfix"></div>
			<span class="submit_btn1" id="header_contact_button"><a  href="#">Cek Layanan Pinjam</a>
			</span>
			<span class="text2_font">Telah Membantu &nbsp;</span><span class="text3_font">10 Juta Jiwa</span> 
		</div>
		<div class="seven columns  omega" ><div class="box_heart1"><img src="homepage-background/heart.png"  alt=""></div><div class="clearfix"></div> </div> 
			<div class="clearfix"></div> 
	</div>
	<div class="clearfix "></div> 
</div>
</div>


									<!--Apa Yang Dikatakan Mereka-->

<div class="clearfix"></div>
<div class="sub_bg_3">
<div class="container top_5">
	<div class="sixteen columns  ">
		<div class="bottom25"><div class="patients_titre">Apa Yang Dikatan Mereka, Tentang Kami</div>
		<div class="sous_header bottom_50"></div></div>
		<div class="clearfix"></div>
	</div>
		<div class="eight columns  alpha border_say" >
			
				<div class=" three columns  alpha " ><img src="testimonials/testi.jpg" alt=""></div>
				<div class="five columns  omega"><div><span class="patients_font" >" Saya Sangat Terbantu Dengan Adanya Pinjaman Uang "</span></div>
				<div><span class="maria">Okhi Sahrul Barkah, 20 Tahun </span></div>
				
				</div>
			
		</div>
	
		<div class="eight columns  omega border_say " >	
			<div class="three columns alpha" ><img src="testimonials/testi.jpg" alt=""></div>	
			<div class="five columns  omega"><div><span class="patients_font">" Saya Sangat Terbantu Dengan Adanya Pinjaman Uang"</span></div>
			<div><span class="maria">Okhi Sahrul Barkah, 20 Tahun </span></div>
			</div>

		</div>
		
		</div>
	</div>
	</div>	
</div>
											<!--Information -->
<div class="sub_bg_1 contact_section">
<div class="container top_5">
	<div class="sixteen columns sub_bg_4">
		<div class="eight columns  alpha " >
			<div><span class="contact_font">Cek Layak Pinjam</span> </div>
			
			<div ><ul class="available_font">
				<li><span >Kami siap membantu finansial anda.</span></li></ul></div>

			<div class="clearfix"></div>
						<fieldset id="contact_form">

						<div id="result"></div>
						    <label for="fname"><span>Nama lengkap *</span><br/> 
						    <input type="text" name="fname" id="fname" />
						    </label>
						    
						    <label for="lname"><span>Jumlah pendapatan per tahun *</span><br/> 
						    <input type="text" name="lname" id="lname" />
						    </label>

						    <label for="email"><span>Jumlah tangunggan *</span><br/> 
						    <input type="email" name="email" id="email" />
						    </label>

						    <label for="email"><span>Durasi pinjaman (Bulan) *</span><br/> 
							<input type="email" name="email" id="email" />
						    </label>

						    <label for="message">Tuliskan Kembali kalimat ini ("Saya Siap pinjam dan siap melunasi") *</label>
									<textarea name="message"  id="message" rows="3"
									cols="30" placeholder=""></textarea>

									
						   	 <button class="submit_btn" id="submit_btn">Submit</button>
						    
						</fieldset>
		</div>
		<div class="eight columns  omega" >
		
			<div><span class="contact_font">Panduan Pengisian</span> </div>
			<div ><ul class="info_font">
				<li><span >Jumlah Pendapatan Per tahun = Hanya tuliskan angka</span></li>
				<li><span >Durasi Tanggunan = Hanya tuliskan angka</span></li>
				<li><span >Durasi pinjaman = Hanya tuliskan angka</span></li> 

		</div>
</div></div></div>

															

<div class="sub_bg_5">
	<div class="container">
	<div class="love_font"><span >Made with <img src="features/heart-small.original.png" alt="img" >  Data Mining | All rights reserved Copyright © 2022 Cek - Layak - Pinjam - OSB</span></div>
</div></div>






<div id="hidden" class="confirm_page">
  <div class="confirm_logo"><span class="pe-7s-check pe-5x pe-va colored"></span></div>
    <div class="confirm_header">Thank You Very Much!</div>
  <div class="confirm_text">
    We turn you on to pro lighting strategies to highlight features create intrigue and make the most of indoor and outdoor rooms
  </div>

  <div class="confirm_social">
          <a href="https://twitter.com/share" class="twitter-share-button" data-via="pixfort" data-count="none">Tweet</a>



<!-- Place this tag where you want the +1 button to render. -->
<span class="confirm_gp">
  <span class="g-plusone " data-size="medium" data-annotation="none"></span>
</span>

<!-- Place this tag after the last +1 button tag. -->



<iframe src="https://www.facebook.com/plugins/like.php?href=http%3A%2F%2Fthemeforest.net%2Fuser%2FPixFort&amp;width&amp;layout=button&amp;action=like&amp;show_faces=false&amp;share=false&amp;height=35&amp;appId=445119778844521" style="border:none; overflow:hidden; height:20px;width:50px;" ></iframe>

        </div>


</div>


<!-- JavaScript
  ================================================== -->

	<script src="js/car/jquery-1.7.2.min.js" type="text/javascript"></script> <!-- jQuery -->
	<script src="js/car/jquery.easing.1.3.js" type="text/javascript"></script> <!-- jQuery easing -->
	<script src="js/car/custom.js" type="text/javascript"></script> <!-- jQuery initialization -->
	<script type='text/javascript' src='js/jquery.common.min.js'></script>
	<script type='text/javascript' src='js/jquery.plugins.js'></script>


  <script>
!function(d,s,id){var js,fjs=d.getElementsByTagName(s)[0],p=/^http:/.test(d.location)?'http':'https';if(!d.getElementById(id)){js=d.createElement(s);js.id=id;js.src=p+'://platform.twitter.com/widgets.js';fjs.parentNode.insertBefore(js,fjs);}}(document, 'script', 'twitter-wjs');
  </script> <script type="text/javascript">
(function() {
    var po = document.createElement('script'); po.type = 'text/javascript'; po.async = true;
    po.src = 'https://apis.google.com/js/platform.js';
    var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(po, s);
  })();
  </script> 

    <!-- End Document
================================================== -->
</body>
</html>
""")
