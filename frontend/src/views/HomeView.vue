<script>
import { FontAwesomeIcon } from '@/plugins/fontawesome'
import { RouterLink } from 'vue-router'
</script>

<template>
  <main class="container-fluid">
    <div id="carouselExampleCaptions" data-bs-ride="carousel" class="carousel slide">
      <div class="carousel-indicators">
        <button type="button" data-bs-target="#carouselExampleCaptions" data-bs-slide-to="0" class="active"
          aria-current="true" aria-label="Slide 1"></button>
        <button type="button" data-bs-target="#carouselExampleCaptions" data-bs-slide-to="1"
          aria-label="Slide 2"></button>
        <button type="button" data-bs-target="#carouselExampleCaptions" data-bs-slide-to="2"
          aria-label="Slide 3"></button>
      </div>
      <div class="carousel-inner">
        <div class="carousel-item active">
          <div class="carousel-caption d-flex flex-column align-items-start">
            <h5 class="animate__animated animate__fadeInDown" style="animation-delay: 1s">
              Encuentra <span>Mesa</span>
            </h5>
            <p class="animate__animated animate__fadeInUp parrafo_inicio_portada" style="animation-delay: 2s">
              Nuestra aplicación simplifica este proceso, permitiéndote buscar mesas en bares
              cercanos de manera fácil y rápida.
            </p>
            <p class="animate__animated animate__fadeInUp" style="animation-delay: 3s">
              <a href="#about" class="btn btn-primary">Saber más</a>
            </p>
          </div>
        </div>
        <div class="carousel-item">
          <div class="carousel-caption d-flex flex-column align-items-start">
            <h5 class="animate__animated animate__fadeInDown" style="animation-delay: 1s">
              Haz <span>Reserva</span>
            </h5>
            <p class="animate__animated animate__fadeInUp parrafo_inicio_portada" style="animation-delay: 2s">
              Podrás reservar mesa y elegir la cantidad de comensales que te acompañaran en tu
              flamante cita.
            </p>
            <p class="animate__animated animate__fadeInUp" style="animation-delay: 3s">
              <a href="#choose" class="btn btn-primary">Saber más</a>
            </p>
          </div>
        </div>
        <div class="carousel-item">
          <div class="carousel-caption d-flex flex-column align-items-start">
            <h5 class="animate__animated animate__fadeInDown" style="animation-delay: 1s">
              No <span>Esperes</span>
            </h5>
            <p class="animate__animated animate__fadeInUp parrafo_inicio_portada" style="animation-delay: 2s">
              Descarga nuestra aplicación y redescubre la forma de disfrutar de tu tiempo en bares y
              restaurantes.
            </p>
            <p class="animate__animated animate__fadeInUp" style="animation-delay: 3s">
              <a href="#choose" class="btn btn-primary">Learn More</a>
            </p>
          </div>
        </div>
      </div>
      <button class="carousel-control-prev" type="button" data-bs-target="#carouselExampleCaptions"
        data-bs-slide="prev">
        <span class="carousel-control-prev-icon" aria-hidden="true"></span>
        <span class="visually-hidden">Previous</span>
      </button>
      <button class="carousel-control-next" type="button" data-bs-target="#carouselExampleCaptions"
        data-bs-slide="next">
        <span class="carousel-control-next-icon" aria-hidden="true"></span>
        <span class="visually-hidden">Next</span>
      </button>
    </div>
    <!--About zone-->
    <div class="about-area section-padding mt-3" id="about">
      <div class="container">
        <div class="row">
          <div class="col-lg-6 col-sm-12">
            <div class="img-area">
              <img src="../assets/about.jpg" alt="joven conversando" />
            </div>
          </div>
          <div class="col-lg-6 col-mg-12">
            <div class="about-text">
              <h2>Somos <span>Personas</span> Innovadoras</h2>
              <p>
                ¿Eres dueño de un bar? ¡No te pierdas la oportunidad de impulsar tu popularidad! Al
                darte de alta en nuestra aplicación, abres las puertas a una mayor visibilidad y
                atraes a nuevos clientes. Nuestra plataforma te conecta con usuarios locales que
                buscan lugares para salir. Con información detallada y la opción de gestionar las
                reservas, tu bar se destacará entre la competencia. Aprovecha la tecnología para
                aumentar tu clientela y ofrecer experiencias memorables. Registra tu bar ahora y sé
                parte de la revolución digital en la industria de la hostelería.
              </p>
              <router-link :to="{ name: 'about' }" class="nav-link"
                router-link-active="active">Contáctanos</router-link>
            </div>
          </div>
        </div>
      </div>
    </div>
    <!-- Services zone-->
    <div class="services section-padding" id="services">
      <div class="container">
        <div class="row">
          <div class="col-lg-12">
            <div class="section-header text-center">
              <h2>Nuestros <span>Servicios</span></h2>
              <p>Lo que ofrecemos actualmente</p>
            </div>
          </div>
        </div>
        <div class="row">
          <div class="col-lg-3 col-md-6 col-sm-6">
            <div class="single-services text-center">
              <font-awesome-icon icon="martini-glass-citrus" class="icon-services"></font-awesome-icon>
              <h2>Promociona Tu Bar</h2>
              <p>
                Beneficiate de la ventaja del turismo en nuestro país, saca ventaja de la
                accesibilidad de nuestra aplicación.
              </p>
            </div>
          </div>
          <div class="col-lg-3 col-md-6 col-sm-6">
            <div class="single-services text-center">
              <font-awesome-icon icon="champagne-glasses" class="icon-services"></font-awesome-icon>
              <h2>Mas Clientes</h2>
              <p>
                La aplicacion esta pensada con especialidad para esos bares que no son capaces de
                aprovechar sus mesas.
              </p>
            </div>
          </div>
          <div class="col-lg-3 col-md-6 col-sm-6">
            <div class="single-services text-center">
              <font-awesome-icon icon="calendar-plus" class="icon-services"></font-awesome-icon>
              <h2>Tu Gestión</h2>
              <p>
                Podrás decidir cuantas mesas dar de altas, ademas de aceptar las reservas
                personalmente...
              </p>
            </div>
          </div>
          <div class="col-lg-3 col-md-6 col-sm-6">
            <div class="single-services text-center">
              <font-awesome-icon icon="wrench" class="icon-services"></font-awesome-icon>
              <h2>Confiable</h2>
              <p>
                Estamos comprometidos a mejorar nuestra oferta actual, asi como revisar cualquier
                fallo en nuestra aplicación.
              </p>
            </div>
          </div>
        </div>
      </div>
    </div>
    <!--Why us zone-->
    <div class="choose section-padding mt-3" id="choose">
      <div class="container">
        <div class="row">
          <div class="col-lg-12">
            <div class="section-header text-center">
              <h2>¿Porqué <span>Escogernos?</span></h2>
              <p>Te damos cuatro opciones</p>
            </div>
          </div>
        </div>
        <div class="row">
          <div class="col-lg-7">
            <div class="choose-area text-center">
              <div class="row">
                <div class="col-lg-6 col-md-6 col-sm-12">
                  <div class="single-box">
                    <font-awesome-icon icon="credit-card" class="icon-why"></font-awesome-icon>
                    <h2>Why <span>Choose Us?</span></h2>
                    <p>Servicio gratuito</p>
                  </div>
                </div>
                <div class="col-lg-6 col-md-6 col-sm-12">
                  <div class="single-box">
                    <font-awesome-icon icon="hand-holding-hand" class="icon-why"></font-awesome-icon>
                    <h2>Why <span>Choose Us?</span></h2>
                    <p>Comprometidos con la asistencia</p>
                  </div>
                </div>
                <div class="col-lg-6 col-md-6 col-sm-12">
                  <div class="single-box">
                    <font-awesome-icon icon="earth" class="icon-why"></font-awesome-icon>
                    <h2>Why <span>Choose Us?</span></h2>
                    <p>Posibilidad de ser buscado desde cualquier sitio del mundo</p>
                  </div>
                </div>
                <div class="col-lg-6 col-md-6 col-sm-12">
                  <div class="single-box">
                    <font-awesome-icon icon="y" class="icon-why"></font-awesome-icon>
                    <h2>Why <span>Choose Us?</span></h2>
                    <p>Aplicacion pionera del mundo a junio de 2024 con estado de mesas libres en tiempo real</p>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div class="col-lg-5 col-sm-12">
            <div class="choose-img">
              <img src="../assets/choose.jpg" alt="imagen sevilla" />
            </div>
          </div>
        </div>
      </div>
    </div>
    <!--Testimonial zone-->
    <div class="testimonial-section padding mt-3 mb-3" id="testi">
      <div class="container">
        <div class="row">
          <div class="col-lg-12">
            <div class="section-header text-center">
              <h2>Comentarios de <span>Usuarios</span></h2>
              <p>Comentarios dejados por usuarios que han buscado mesa o dueños de bares en la aplicación</p>
            </div>
          </div>
        </div>
        <div class="row">
          <div class="col-lg-4 col-sm-12">
            <div class="single-client text-center">
              <div class="imgBox">
                <img src="../assets/cara1.jpg" alt="" />
              </div>
              <h2>John Doe</h2>
              <p>
                <i>"Aproveche las promociones de las ofertas para empezar a atraer clientes que al conocer el bar por
                  primera vez, repitieron!"</i>
              </p>
              <h5>GERENTE <br /><span>Bar los álamos</span></h5>
            </div>
          </div>
          <div class="col-lg-4 col-sm-12">
            <div class="single-client text-center">
              <div class="imgBox">
                <img src="../assets/cara2.jpg" alt="" />
              </div>
              <h2>John Doe</h2>
              <p>
                <i>"En una ciudad con tanto turismo como Sevilla, esta aplicación me hace saber si puedo tomarme algo en
                  el centro o no"</i>
              </p>
              <h5>CONSUMIDOR <br /><span>Local</span></h5>
            </div>
          </div>
          <div class="col-lg-4 col-sm-12">
            <div class="single-client text-center">
              <div class="imgBox">
                <img src="../assets/cara3.jpg" alt="" />
              </div>
              <h2>John Doe</h2>
              <p>
                <i>"Antes de decidir escoger el hotel en el que me estuve hospedando en Madrid comprobé si los bares
                  suelen estar llenos alrededor"</i>
              </p>
              <h5>CONSUMIDOR <br /><span>Extranjero</span></h5>
            </div>
          </div>
        </div>
      </div>
    </div>
  </main>
</template>
<style scoped>
* {
  font-family: montserrat;
}

/* carousel */
.carousel {
  background-image: url(../assets/home.jpg);
  background-size: cover;
  background-position: center;
}

.carousel-item {
  height: 100vh;
  min-height: 300px;
}

.carousel-caption {
  display: flex;
  flex-direction: column;
  align-items: start;
  max-width: 60%;
  border-radius: 10px;
  background: rgba(255, 255, 255, 0.6);
  bottom: 20%;
  z-index: 2;
  left: 5%;
  padding: 20px;
}

.carousel-caption h5 {
  font-size: 2.5rem;
  margin-top: 0;
  color: #08194a;
  font-weight: 700;
  text-align: left;
}

.carousel-caption span {
  color: #e53f29;
  font-weight: 900;
}

.carousel-caption p {
  font-size: 1.25rem;
  line-height: 1.8;
  color: #08194a;
  text-align: left;
  margin-bottom: 20px;
}

.carousel-caption a.btn {
  text-transform: uppercase;
  text-decoration: none;
  background: #08194a;
  padding: 10px 20px;
  display: inline-block;
  color: #fff;
  border-radius: 5px;
}


.parrafo_inicio_portada {
  font-weight: 700;
  letter-spacing: 0.5px;
  text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.2);
  color: darkslategray !important;
  font-size: 1.5em;
  /* Ajuste del tamaño de la fuente para mayor visibilidad */
  border-left: 5px solid #08194a;
  padding-left: 10px;
}

.carousel-caption a {
  text-transform: uppercase;
  text-decoration: none;
  background: #08194a;
  padding: 5px 20px;
  display: inline-block;
  color: #fff;
  margin-top: 15px;
  border-radius: 5px;
}

/*About(second) zone */
.img-area img {
  width: 100% !important;
}

.about-text h2 {
  font-size: 45px;
  font-weight: 700;
  color: #08194a;
}

.about-text h2 span {
  color: #e53f29;
}

.about-text a {
  text-transform: uppercase;
  text-decoration: none;
  background: #08194a;
  padding: 5px 20px;
  display: inline-block;
  color: #fff;
  border-radius: 5px;
}

.about-text p {
  font-size: large;
}

/*Services zone */
.section-header {
  margin-bottom: 40px;
}

.section-header h2 {
  color: #08194a;
  font-size: 45px;
  font-weight: 700;
}

.section-header span {
  color: #e53f29;
}

.section-header p {
  font-size: large;
}

.single-services {
  background: #08194a;
  color: #fff;
  padding: 30px 15px;
}

.icon-services {
  font-size: 45px;
  margin-bottom: 30px;
}

.single-services h2 {
  font-family: fantasy;
}

/*Why Us zone */
.choose-img img {
  width: 80%;
  padding-left: 30%;
}

.single-box {
  padding: 20px;
}

.icon-why {
  font-size: 35px;
  margin-bottom: 25px;
  color: #e53f29;
}

.single-box h2 {
  font-family: fantasy;
  color: #08194a;
}

.single-box p {
  text-decoration: none;
  background: whitesmoke;
  padding: 1px 20px;
  display: inline-block;
  color: indianred;
  border-radius: 3px;
  font-size: 110%;
}

/* Testimonial Zone */
.imgBox {
  width: 80px;
  height: 80px;
  overflow: hidden;
  border-radius: 50%;
  margin: 0 auto 25px;
}

.imgBox img {
  width: 100%;
}

.single-client {
  box-shadow: 0 2px 20px rgba(0, 0, 0, 0.3);
  padding: 30px 15px;
}

.single-client h2 {
  color: #08194a;
  font-family: fantasy;
}

.single-client h5 {
  color: #08194a;
  font-weight: 600;
  font-size: 15px;
}

.single-client h5 span {
  font-size: 12px;
  text-transform: uppercase;
}
</style>
