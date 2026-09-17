/* ============================================================================
   Zyntra - comportamiento del sitio.

   Vanilla, sin dependencias, con defer. Todo lo que anima respeta
   prefers-reduced-motion: es regla del sistema, no un extra.
   ========================================================================== */
(function () {
    'use strict';

    var quieto = window.matchMedia('(prefers-reduced-motion: reduce)');

    /* ---------------------------------------------------------- 1. header */

    var header = document.querySelector('.site-header');
    var progreso = document.getElementById('scroll-progress');

    function alScrollear() {
        var y = window.pageYOffset || document.documentElement.scrollTop;
        if (header) header.classList.toggle('is-scrolled', y > 8);
        if (progreso) {
            var alto = document.documentElement.scrollHeight - window.innerHeight;
            progreso.style.width = (alto > 0 ? (y / alto) * 100 : 0) + '%';
        }
    }

    if (header || progreso) {
        alScrollear();
        window.addEventListener('scroll', alScrollear, { passive: true });
        window.addEventListener('resize', alScrollear, { passive: true });
    }

    /* ----------------------------------------------------- 2. menu mobile */

    var toggle = document.getElementById('menu-toggle');
    var menu = document.getElementById('mobile-menu');

    if (toggle && menu) {
        var cerrar = function () {
            menu.hidden = true;
            toggle.setAttribute('aria-expanded', 'false');
            toggle.setAttribute('aria-label', 'Abrir menú');
        };
        toggle.addEventListener('click', function () {
            var abierto = menu.hidden;
            menu.hidden = !abierto;
            toggle.setAttribute('aria-expanded', abierto ? 'true' : 'false');
            toggle.setAttribute('aria-label', abierto ? 'Cerrar menú' : 'Abrir menú');
        });
        Array.prototype.forEach.call(menu.querySelectorAll('a'), function (a) {
            a.addEventListener('click', cerrar);
        });
        document.addEventListener('keydown', function (e) {
            if (e.key === 'Escape' && !menu.hidden) { cerrar(); toggle.focus(); }
        });
        window.addEventListener('resize', function () {
            if (window.innerWidth >= 900 && !menu.hidden) cerrar();
        }, { passive: true });
    }

    /* --------------------------------------------------------- 3. reveal */

    var revelables = document.querySelectorAll('.reveal');
    if (revelables.length) {
        if (quieto.matches || !('IntersectionObserver' in window)) {
            Array.prototype.forEach.call(revelables, function (el) { el.classList.add('visible'); });
        } else {
            var obs = new IntersectionObserver(function (entradas) {
                entradas.forEach(function (e) {
                    if (e.isIntersecting) { e.target.classList.add('visible'); obs.unobserve(e.target); }
                });
            }, { rootMargin: '0px 0px -60px 0px', threshold: 0.05 });
            Array.prototype.forEach.call(revelables, function (el) { obs.observe(el); });
        }
    }

    /* ---------------------------------------------------- 4. calculadora */

    /* La cuenta es la misma de siempre y se mantiene a proposito:
       caidas por semana x ticket x 52. No es una promesa de resultado. */
    (function () {
        var volumen = document.getElementById('calc-volumen');
        var perdidos = document.getElementById('calc-perdidos');
        var ticket = document.getElementById('calc-ticket');
        var anual = document.getElementById('calc-anual');
        var detalle = document.getElementById('calc-detalle');
        if (!volumen || !perdidos || !ticket || !anual) return;

        var pesos = new Intl.NumberFormat('es-AR', {
            style: 'currency', currency: 'ARS', maximumFractionDigits: 0
        });

        function num(el) {
            var v = parseFloat(el.value);
            return isFinite(v) && v > 0 ? v : 0;
        }

        function calcular() {
            var v = num(volumen), p = num(perdidos), t = num(ticket);
            if (p > v) { p = v; }                    // no se pueden perder mas de las que hay
            anual.textContent = pesos.format(p * t * 52);
            if (detalle) {
                detalle.innerHTML = p
                    ? 'Son <strong>' + p + (p === 1 ? ' oportunidad' : ' oportunidades') +
                      ' por semana</strong> que se pierden. Un sistema de recordatorios y ' +
                      'seguimiento automático recupera buena parte de eso.'
                    : 'Si de verdad no se te cae ninguna, no necesitás contratarnos. ' +
                      'Probá con tus números reales.';
            }
        }

        [volumen, perdidos, ticket].forEach(function (el) {
            el.addEventListener('input', calcular);
        });
        calcular();
    }());

    /* ------------------------------------------------------ 5. carruseles */

    Array.prototype.forEach.call(document.querySelectorAll('[data-carousel]'), function (caja) {
        var slides = caja.querySelectorAll('.carousel-slide');
        var puntos = caja.querySelectorAll('.carousel-dot');
        if (slides.length < 2) return;
        var actual = 0;

        function ir(i) {
            actual = (i + slides.length) % slides.length;
            Array.prototype.forEach.call(slides, function (s, n) {
                s.classList.toggle('active', n === actual);
            });
            Array.prototype.forEach.call(puntos, function (p, n) {
                p.classList.toggle('active', n === actual);
                p.setAttribute('aria-current', n === actual ? 'true' : 'false');
            });
        }

        Array.prototype.forEach.call(puntos, function (p, n) {
            p.addEventListener('click', function () { ir(n); });
        });

        // deslizar con el dedo
        var x0 = null;
        caja.addEventListener('touchstart', function (e) { x0 = e.touches[0].clientX; }, { passive: true });
        caja.addEventListener('touchend', function (e) {
            if (x0 === null) return;
            var d = e.changedTouches[0].clientX - x0;
            if (Math.abs(d) > 45) ir(actual + (d < 0 ? 1 : -1));
            x0 = null;
        }, { passive: true });
    });

    /* ---------------------------------------------------------- 6. Ojito */

    /* Dos comportamientos y nada mas: parpadea cada 4-7 segundos y el iris
       sigue al cursor dentro de un radio de 0.12 del diametro. El parpado es
       la unica expresion que tiene: no le agregues nada. */
    var ojitos = document.querySelectorAll('[data-ojito]');

    if (ojitos.length && !quieto.matches) {

        Array.prototype.forEach.call(ojitos, function (ojo) {
            function parpadear() {
                ojo.classList.add('parpadea');
                setTimeout(function () { ojo.classList.remove('parpadea'); }, 150);
                setTimeout(parpadear, 4000 + Math.random() * 3000);
            }
            setTimeout(parpadear, 1500 + Math.random() * 3000);
        });

        var pendiente = false;
        window.addEventListener('pointermove', function (e) {
            if (pendiente) return;
            pendiente = true;
            requestAnimationFrame(function () {
                pendiente = false;
                Array.prototype.forEach.call(ojitos, function (ojo) {
                    var cuerpo = ojo.querySelector('.ojito-cuerpo');
                    var iris = ojo.querySelector('.ojito-iris');
                    if (!cuerpo || !iris) return;
                    var r = cuerpo.getBoundingClientRect();
                    if (r.width === 0) return;
                    var dx = e.clientX - (r.left + r.width / 2);
                    var dy = e.clientY - (r.top + r.height / 2);
                    var dist = Math.sqrt(dx * dx + dy * dy) || 1;
                    var max = r.width * 0.12;
                    var k = Math.min(1, dist / (r.width * 1.6));
                    ojo.style.setProperty('--iris-x', (dx / dist) * max * k + 'px');
                    ojo.style.setProperty('--iris-y', (dy / dist) * max * k + 'px');
                });
            });
        }, { passive: true });
    }

    /* -------------------------------------------- 7. acordeon de frentes */

    /* El acordeon es nativo: <details name="frentes"> ya cierra los hermanos
       solo. Esto es el respaldo para los navegadores que todavia no lo
       soportan, mas el scroll para que al abrir uno de abajo no te quede el
       titulo tapado por el header. */
    (function () {
        var frentes = document.querySelectorAll('details.acordeon[name]');
        if (!frentes.length) return;

        var nativo = 'name' in document.createElement('details');

        Array.prototype.forEach.call(frentes, function (d) {
            d.addEventListener('toggle', function () {
                if (!d.open) return;

                if (!nativo) {
                    // hay dos grupos, "frentes" y "proyectos": solo se cierran
                    // los del mismo. Se compara por atributo porque justamente
                    // aca la propiedad .name no existe.
                    var grupo = d.getAttribute('name');
                    Array.prototype.forEach.call(frentes, function (otro) {
                        if (otro !== d && otro.getAttribute('name') === grupo) otro.open = false;
                    });
                }

                // si el titulo quedo arriba del viewport, traerlo de vuelta
                if (!quieto.matches) {
                    requestAnimationFrame(function () {
                        var y = d.getBoundingClientRect().top;
                        if (y < 80 || y > window.innerHeight - 120) {
                            window.scrollTo({
                                top: window.pageYOffset + y - 88,
                                behavior: 'smooth'
                            });
                        }
                    });
                }
            });
        });
    }());

    /* ------------------------------------- 9. secciones que se deslizan */

    /* OJO, no confundir con el punto 5: aquel ([data-carousel], en ingles)
       es la galeria de capturas DENTRO de cada proyecto. Este
       ([data-carrusel], en castellano) desliza las tarjetas de una seccion
       entera: industrias, frentes y portfolio.

       El HTML no trae flechas ni puntos, los pone este script. Por eso el
       CSS del carrusel cuelga de data-listo: si este codigo no corre, la
       pista queda como grilla y se ve todo, en vez de una sola tarjeta sin
       forma de avanzar. */

    Array.prototype.forEach.call(document.querySelectorAll('[data-carrusel]'), function (caja) {
        var pista = caja.querySelector('.carrusel-pista');
        if (!pista) return;
        var items = Array.prototype.slice.call(pista.children);
        if (items.length < 2) return;

        // Estas tarjetas traen .reveal y arrancan en opacity 0. Dentro de una
        // pista horizontal las que estan mas alla quedan recortadas, asi que
        // el IntersectionObserver no dispara hasta que llegan y se veria el
        // fade en cada flechazo. Se las muestra de entrada.
        items.forEach(function (el) {
            el.classList.add('visible');
            Array.prototype.forEach.call(el.querySelectorAll('.reveal'), function (h) {
                h.classList.add('visible');
            });
        });

        caja.setAttribute('data-listo', '');

        function porVista() {
            return parseInt(getComputedStyle(caja).getPropertyValue('--por-vista'), 10) || 1;
        }
        function paginas() { return Math.ceil(items.length / porVista()); }
        function origen(i) { return items[i].offsetLeft - items[0].offsetLeft; }

        function indice() {
            var x = pista.scrollLeft;
            var mejor = 0, dist = Infinity;
            for (var i = 0; i < items.length; i++) {
                var d = Math.abs(origen(i) - x);
                if (d < dist) { dist = d; mejor = i; }
            }
            return Math.min(paginas() - 1, Math.floor(mejor / porVista()));
        }

        function irA(pagina) {
            var p = Math.max(0, Math.min(paginas() - 1, pagina));
            pista.scrollTo({
                left: origen(p * porVista()),
                behavior: quieto.matches ? 'auto' : 'smooth'
            });
        }

        function flecha(clase, etiqueta, salto) {
            var b = document.createElement('button');
            b.type = 'button';
            b.className = 'carrusel-flecha ' + clase;
            b.setAttribute('aria-label', etiqueta);
            b.innerHTML = '<svg class="ico" aria-hidden="true"><use href="#i-flecha"></use></svg>';
            b.addEventListener('click', function () { irA(indice() + salto); });
            return b;
        }

        // Dos juegos de flechas: el CSS muestra el del costado en escritorio
        // y el del pie en telefono, donde al costado se comerian el ancho.
        var izqLado = flecha('carrusel-flecha--izq', 'Anterior', -1);
        var derLado = flecha('carrusel-flecha--der', 'Siguiente', 1);
        caja.appendChild(izqLado);
        caja.appendChild(derLado);

        var pie = document.createElement('div');
        pie.className = 'carrusel-pie';
        var izqPie = flecha('carrusel-flecha--izq', 'Anterior', -1);
        var derPie = flecha('carrusel-flecha--der', 'Siguiente', 1);
        var puntos = document.createElement('div');
        puntos.className = 'carrusel-puntos';
        var cuenta = document.createElement('span');
        cuenta.className = 'carrusel-cuenta';
        cuenta.setAttribute('aria-live', 'polite');
        pie.appendChild(izqPie);
        pie.appendChild(puntos);
        pie.appendChild(cuenta);
        pie.appendChild(derPie);
        caja.appendChild(pie);

        var flechas = [izqLado, izqPie, derLado, derPie];
        var bolitas = [];

        function armarPuntos() {
            var n = paginas();
            if (bolitas.length === n) return;
            puntos.innerHTML = '';
            bolitas = [];
            for (var i = 0; i < n; i++) {
                (function (i) {
                    var b = document.createElement('button');
                    b.type = 'button';
                    b.className = 'carrusel-punto';
                    b.setAttribute('aria-label', 'Ir a ' + (i + 1) + ' de ' + n);
                    b.addEventListener('click', function () { irA(i); });
                    puntos.appendChild(b);
                    bolitas.push(b);
                }(i));
            }
        }

        function pintar() {
            armarPuntos();
            var i = indice();
            var n = paginas();
            bolitas.forEach(function (b, k) {
                b.setAttribute('aria-current', k === i ? 'true' : 'false');
            });
            cuenta.textContent = (i + 1) + ' de ' + n;
            izqLado.disabled = izqPie.disabled = i <= 0;
            derLado.disabled = derPie.disabled = i >= n - 1;
        }

        // Se regula con setTimeout y no con requestAnimationFrame a proposito:
        // rAF queda suspendido mientras la pestana esta en segundo plano, y
        // como el flag nunca se libera, los puntos y el contador se quedan
        // clavados en la posicion vieja. Aca no se anima nada, solo se
        // actualizan textos y clases, asi que un timer alcanza y siempre corre.
        var pendiente = null;
        pista.addEventListener('scroll', function () {
            if (pendiente) return;
            pendiente = setTimeout(function () { pendiente = null; pintar(); }, 60);
        }, { passive: true });

        window.addEventListener('resize', function () {
            bolitas = [];          // cambia el por-vista, cambian las paginas
            pintar();
        });

        pintar();
    });

    /* ------------------------------------------------- 8. año del footer */

    Array.prototype.forEach.call(document.querySelectorAll('[data-anio]'), function (el) {
        el.textContent = new Date().getFullYear();
    });

}());
