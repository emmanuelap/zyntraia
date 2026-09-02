/* Zyntra - comportamiento del sitio.
   Se carga al final del body, en el mismo orden en que estaba inline. */

const siteHeader = document.querySelector('.site-header');
        const scrollBar  = document.getElementById('scroll-progress');

        function updateHeaderState() {
            if (siteHeader) {
                siteHeader.classList.toggle('is-scrolled', window.scrollY > 24);
            }
            if (scrollBar) {
                var max = document.documentElement.scrollHeight - window.innerHeight;
                var pct = max > 0 ? (window.scrollY / max) * 100 : 0;
                scrollBar.style.width = Math.min(100, Math.max(0, pct)) + '%';
            }
        }

        updateHeaderState();
        window.addEventListener('scroll', updateHeaderState, { passive: true });
        window.addEventListener('resize', updateHeaderState, { passive: true });

        // ===== CAROUSELS (manuales: los pasa el visitante, no se mueven solos) =====
        document.querySelectorAll('[data-carousel]').forEach(function(container) {
            var slides = Array.from(container.querySelectorAll('.carousel-slide'));
            var dots   = Array.from(container.querySelectorAll('.carousel-dot'));
            if (!slides.length) return;
            var current = 0;

            function goTo(n) {
                slides[current].classList.remove('active');
                if (dots[current]) dots[current].classList.remove('active');
                current = ((n % slides.length) + slides.length) % slides.length;
                slides[current].classList.add('active');
                if (dots[current]) dots[current].classList.add('active');
                if (contador) contador.textContent = (current + 1) + ' / ' + slides.length;
            }

            dots.forEach(function(dot, i) {
                dot.addEventListener('click', function() { goTo(i); });
            });

            var contador = null;
            if (slides.length > 1) {
                // Las flechas van absolutas: el contenedor tiene que ser el ancestro posicionado.
                if (getComputedStyle(container).position === 'static') {
                    container.style.position = 'relative';
                }

                // Flechas
                [['prev', 'chevron_left', 'Imagen anterior'],
                 ['next', 'chevron_right', 'Imagen siguiente']].forEach(function(cfg) {
                    var b = document.createElement('button');
                    b.type = 'button';
                    b.className = 'carousel-nav ' + cfg[0];
                    b.setAttribute('aria-label', cfg[2]);
                    b.innerHTML = '<span class="material-symbols-outlined" aria-hidden="true">' + cfg[1] + '</span>';
                    b.addEventListener('click', function(e) {
                        e.preventDefault();
                        goTo(current + (cfg[0] === 'next' ? 1 : -1));
                    });
                    container.appendChild(b);
                });

                // Contador
                contador = document.createElement('span');
                contador.className = 'carousel-count';
                contador.textContent = '1 / ' + slides.length;
                container.appendChild(contador);

                // Teclado, cuando el carrusel tiene el foco
                container.setAttribute('tabindex', '0');
                container.setAttribute('role', 'group');
                container.setAttribute('aria-label', 'Galería del proyecto');
                container.addEventListener('keydown', function(e) {
                    if (e.key === 'ArrowLeft')  { e.preventDefault(); goTo(current - 1); }
                    if (e.key === 'ArrowRight') { e.preventDefault(); goTo(current + 1); }
                });

                // Deslizar con el dedo en celular
                var x0 = null;
                container.addEventListener('touchstart', function(e) {
                    x0 = e.changedTouches[0].clientX;
                }, { passive: true });
                container.addEventListener('touchend', function(e) {
                    if (x0 === null) return;
                    var dx = e.changedTouches[0].clientX - x0;
                    if (Math.abs(dx) > 40) goTo(current + (dx < 0 ? 1 : -1));
                    x0 = null;
                }, { passive: true });
            }
        });

        // ===== SCROLL REVEAL =====
        var revealObs = new IntersectionObserver(function(entries) {
            entries.forEach(function(e) {
                if (e.isIntersecting) {
                    // respect transition-delay set inline
                    e.target.classList.add('visible');
                    revealObs.unobserve(e.target);
                }
            });
        }, { threshold: 0.08, rootMargin: '0px 0px -30px 0px' });

        document.querySelectorAll('.reveal').forEach(function(el) { revealObs.observe(el); });

        // ===== PUERTAS POR INDUSTRIA: resaltar el servicio de destino =====
        (function () {
            var t;
            function destacar() {
                var id = location.hash.replace('#', '');
                if (!id) return;
                var el = document.getElementById(id);
                if (!el || !el.classList.contains('svc-card')) return;
                clearTimeout(t);
                el.classList.remove('destacado');
                void el.offsetWidth;            // reinicia la animacion si se repite el mismo destino
                el.classList.add('destacado');
                t = setTimeout(function () { el.classList.remove('destacado'); }, 3000);
            }
            window.addEventListener('hashchange', destacar);
            if (location.hash) setTimeout(destacar, 260);
        })();

        // ===== MENU MOBILE =====
        (function () {
            var toggle = document.getElementById('menu-toggle');
            var menu   = document.getElementById('mobile-menu');
            var icon   = document.getElementById('menu-icon');
            if (!toggle || !menu) return;

            function setMenu(open) {
                menu.hidden = !open;
                toggle.setAttribute('aria-expanded', open ? 'true' : 'false');
                if (icon) icon.textContent = open ? 'close' : 'menu';
            }

            function closeMenu() { setMenu(false); }

            toggle.addEventListener('click', function () {
                setMenu(menu.hidden);
            });

            menu.querySelectorAll('a').forEach(function (link) {
                link.addEventListener('click', closeMenu);
            });

            document.addEventListener('keydown', function (e) {
                if (e.key === 'Escape') closeMenu();
            });
        })();

        // ===== CALCULADORA DE PERDIDAS =====
        (function () {
            var vol    = document.getElementById('calc-volumen');
            var perd   = document.getElementById('calc-perdidos');
            var ticket = document.getElementById('calc-ticket');
            var anual  = document.getElementById('calc-anual');
            var detalle = document.getElementById('calc-detalle');
            if (!vol || !perd || !ticket || !anual) return;

            var fmt = new Intl.NumberFormat('es-AR', {
                style: 'currency', currency: 'ARS', maximumFractionDigits: 0
            });

            function num(el) {
                var n = parseFloat(el.value);
                return isNaN(n) || n < 0 ? 0 : n;
            }

            function calcular() {
                var volumen  = num(vol);
                var perdidos = Math.min(num(perd), volumen);
                var precio   = num(ticket);
                var porAnio  = perdidos * precio * 52;

                anual.textContent = fmt.format(porAnio);

                if (!detalle) return;
                if (porAnio <= 0) {
                    detalle.innerHTML = 'Completá los tres campos con tus números reales para ver la estimación.';
                } else {
                    var uno = perdidos === 1;
                    detalle.innerHTML = (uno ? 'Es ' : 'Son ') +
                        '<strong class="text-on-surface">' + perdidos +
                        (uno ? ' oportunidad' : ' oportunidades') +
                        ' por semana</strong> que ' + (uno ? 'se pierde' : 'se pierden') +
                        '. Un sistema de recordatorios y seguimiento automático recupera buena parte de eso.';
                }
            }

            [vol, perd, ticket].forEach(function (el) {
                el.addEventListener('input', calcular);
            });
            calcular();
        })();

/* ------------------------------------------------------------------ */

/* =====================================================================
       MOTION IA — corazón reactivo del hero
       Un solo estado (bpm + paleta + capas) que se escribe como custom
       properties sobre #hcEscena. El SVG y el panel leen de ahí.
       ===================================================================== */
    (function () {
        var escena = document.getElementById('hcEscena');
        var svg = document.getElementById('hcSvg');
        if (!escena || !svg) return;

        var suave = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

        var PALETAS = [
            { id: 'cian', nombre: 'Cian Zyntra', punto: '#81ecff', v: {
                '--hc-c0': '#e6fbff', '--hc-c1': '#81ecff', '--hc-c2': '#2f7fc8', '--hc-c3': '#12305f',
                '--hc-w1': '#ffd08a', '--hc-w2': '#f6ae55', '--hc-chip': '#0b2731',
                '--hc-nucleo': '#10d5ff', '--hc-glow': 'rgba(129,236,255,.22)' },
                m: { '--marca': '129 236 255', '--marca-2': '16 213 255', '--marca-dim': '0 212 236', '--marca-txt': '0 56 64' } },
            { id: 'esmeralda', nombre: 'Esmeralda bioluminiscente', punto: '#4dffb8', v: {
                '--hc-c0': '#e3fff3', '--hc-c1': '#4dffb8', '--hc-c2': '#17a06a', '--hc-c3': '#04331f',
                '--hc-w1': '#d9ffab', '--hc-w2': '#8ce06a', '--hc-chip': '#06291d',
                '--hc-nucleo': '#16f0a0', '--hc-glow': 'rgba(77,255,184,.22)' },
                m: { '--marca': '77 255 184', '--marca-2': '22 240 160', '--marca-dim': '0 214 148', '--marca-txt': '0 48 32' } },
            { id: 'violeta', nombre: 'Violeta cuántico', punto: '#b18cff', v: {
                '--hc-c0': '#f2ecff', '--hc-c1': '#b18cff', '--hc-c2': '#6a3fc0', '--hc-c3': '#1b1042',
                '--hc-w1': '#ffb0e8', '--hc-w2': '#e060c8', '--hc-chip': '#170c2c',
                '--hc-nucleo': '#9a5cff', '--hc-glow': 'rgba(177,140,255,.24)' },
                m: { '--marca': '177 140 255', '--marca-2': '154 92 255', '--marca-dim': '138 92 255', '--marca-txt': '26 8 60' } },
            { id: 'ambar', nombre: 'Ámbar solar', punto: '#ffc46b', v: {
                '--hc-c0': '#fff4e0', '--hc-c1': '#ffc46b', '--hc-c2': '#c9762c', '--hc-c3': '#35190a',
                '--hc-w1': '#ffe9a8', '--hc-w2': '#ff9d2e', '--hc-chip': '#241205',
                '--hc-nucleo': '#ff9d2e', '--hc-glow': 'rgba(255,196,107,.22)' },
                m: { '--marca': '255 196 107', '--marca-2': '255 176 66', '--marca-dim': '255 157 46', '--marca-txt': '58 30 0' } },
            { id: 'carmesi', nombre: 'Carmesí vital', punto: '#ff7b8a', v: {
                '--hc-c0': '#ffeaee', '--hc-c1': '#ff7b8a', '--hc-c2': '#c8304f', '--hc-c3': '#3a0714',
                '--hc-w1': '#ffc2a0', '--hc-w2': '#ff7a4d', '--hc-chip': '#26060e',
                '--hc-nucleo': '#ff3d5e', '--hc-glow': 'rgba(255,123,138,.24)' },
                m: { '--marca': '255 123 138', '--marca-2': '255 94 116', '--marca-dim': '255 61 94', '--marca-txt': '62 6 20' } }
        ];

        var bpm = 75;
        var latidos = 0;
        var pulsos = 0;

        /* ---------- largo real de la silueta, para el dibujado ---------- */
        var sil = document.getElementById('hcSilueta');
        if (sil && sil.getTotalLength) {
            escena.style.setProperty('--hc-largo', Math.ceil(sil.getTotalLength()));
        }

        /* ---------- BPM ---------- */
        var salidaBpm = document.getElementById('hcBpmOut');
        var etiquetaBpm = document.getElementById('hcBpmEtiqueta');
        var rango = document.getElementById('hcBpm');

        function aplicarBpm(v, desdeRango) {
            bpm = Math.min(160, Math.max(40, Math.round(v)));
            escena.style.setProperty('--hc-dur', (60 / bpm).toFixed(4) + 's');
            if (salidaBpm) salidaBpm.textContent = bpm;
            if (etiquetaBpm) etiquetaBpm.textContent = bpm;
            if (rango) {
                if (!desdeRango) rango.value = bpm;
                rango.style.setProperty('--hc-pct', ((bpm - 40) / 120 * 100).toFixed(1) + '%');
            }
            [].forEach.call(escena.querySelectorAll('[data-hc-bpm]'), function (b) {
                b.setAttribute('aria-pressed', Number(b.dataset.hcBpm) === bpm ? 'true' : 'false');
            });
            refrescarTelemetria();
        }

        if (rango) rango.addEventListener('input', function () { aplicarBpm(this.value, true); });
        [].forEach.call(escena.querySelectorAll('[data-hc-bpm]'), function (b) {
            b.addEventListener('click', function () { aplicarBpm(Number(b.dataset.hcBpm)); });
        });

        /* ---------- paletas ---------- */
        var cajaPaletas = document.getElementById('hcPaletas');
        var nombrePaleta = document.getElementById('hcPaletaNombre');

        var raiz = document.documentElement;

        function aplicarPaleta(p) {
            for (var k in p.v) { if (Object.prototype.hasOwnProperty.call(p.v, k)) escena.style.setProperty(k, p.v[k]); }
            /* los canales de marca viven en :root, asi el acento de toda la
               web (titulos, botones, bordes, iconos) sigue a la paleta. */
            for (var m in p.m) { if (Object.prototype.hasOwnProperty.call(p.m, m)) raiz.style.setProperty(m, p.m[m]); }
            if (nombrePaleta) nombrePaleta.textContent = p.nombre;
            if (cajaPaletas) {
                [].forEach.call(cajaPaletas.children, function (b) {
                    b.setAttribute('aria-pressed', b.dataset.hcPaleta === p.id ? 'true' : 'false');
                });
            }
        }

        if (cajaPaletas) {
            PALETAS.forEach(function (p) {
                var b = document.createElement('button');
                b.type = 'button';
                b.className = 'hc-swatch';
                b.dataset.hcPaleta = p.id;
                b.style.background = p.punto;
                b.title = p.nombre;
                b.setAttribute('aria-label', 'Paleta ' + p.nombre);
                b.setAttribute('aria-pressed', p.id === 'cian' ? 'true' : 'false');
                b.addEventListener('click', function () { aplicarPaleta(p); });
                cajaPaletas.appendChild(b);
            });
        }

        /* ---------- capas ---------- */
        var CLASE_CAPA = {
            pcb: 'hc-sin-pcb',
            particulas: 'hc-sin-particulas',
            aura: 'hc-sin-aura'
        };
        [].forEach.call(escena.querySelectorAll('[data-hc-capa]'), function (b) {
            b.addEventListener('click', function () {
                var activo = b.getAttribute('aria-pressed') !== 'true';
                b.setAttribute('aria-pressed', activo ? 'true' : 'false');
                var capa = b.dataset.hcCapa;
                if (capa === 'holograma') {
                    escena.classList.toggle('hc-holograma', activo);
                } else {
                    escena.classList.toggle(CLASE_CAPA[capa], !activo);
                }
            });
        });

        /* ---------- telemetría ---------- */
        var elSinapsis = document.getElementById('hcSinapsis');
        var elCoherencia = document.getElementById('hcCoherencia');
        var elLatidos = document.getElementById('hcLatidos');
        var elPulsos = document.getElementById('hcPulsos');

        function refrescarTelemetria() {
            if (elSinapsis) {
                var s = bpm * 428 * (0.985 + Math.random() * 0.03);
                elSinapsis.textContent = (s / 1000).toFixed(1) + 'k';
            }
            if (elCoherencia) {
                var c = 99.9 - Math.abs(bpm - 72) * 0.055 - Math.random() * 0.06;
                elCoherencia.textContent = Math.max(92, c).toFixed(1);
            }
        }

        /* ---------- onda de choque ---------- */
        var capaOndas = document.getElementById('hcOndas');
        function emitirOnda() {
            if (suave || !capaOndas) return;
            var c = document.createElementNS('http://www.w3.org/2000/svg', 'circle');
            c.setAttribute('cx', '232');
            c.setAttribute('cy', '300');
            c.setAttribute('r', '120');
            c.setAttribute('class', 'hc-onda');
            capaOndas.appendChild(c);
            setTimeout(function () { if (c.parentNode) c.parentNode.removeChild(c); }, 950);
        }

        function pulsoManual() {
            pulsos++;
            if (elPulsos) elPulsos.textContent = pulsos;
            emitirOnda();
            refrescarTelemetria();
        }
        svg.addEventListener('click', pulsoManual);
        svg.addEventListener('keydown', function (e) {
            if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); pulsoManual(); }
        });

        /* ---------- reloj del corazón ---------- */
        var acumulado = 0, ultimo = 0, acumTele = 0;
        function tic(t) {
            if (!ultimo) ultimo = t;
            var dt = Math.min(t - ultimo, 250);
            ultimo = t;

            acumulado += dt;
            var periodo = 60000 / bpm;
            while (acumulado >= periodo) {
                acumulado -= periodo;
                latidos++; pulsos++;
                if (elLatidos) elLatidos.textContent = latidos;
                if (elPulsos) elPulsos.textContent = pulsos;
            }

            acumTele += dt;
            if (acumTele >= 900) { acumTele = 0; refrescarTelemetria(); }

            requestAnimationFrame(tic);
        }
        requestAnimationFrame(tic);

        /* ---------- parallax ---------- */
        if (!suave && window.matchMedia('(pointer:fine)').matches) {
            var tx = 0, ty = 0, cx = 0, cy = 0, corriendo = false;
            escena.addEventListener('pointermove', function (e) {
                var r = escena.getBoundingClientRect();
                tx = ((e.clientX - r.left) / r.width) * 2 - 1;
                ty = ((e.clientY - r.top) / r.height) * 2 - 1;
                if (!corriendo) { corriendo = true; requestAnimationFrame(suavizar); }
            });
            escena.addEventListener('pointerleave', function () { tx = 0; ty = 0; });
            var suavizar = function () {
                cx += (tx - cx) * 0.07; cy += (ty - cy) * 0.07;
                escena.style.setProperty('--hc-mx', cx.toFixed(4));
                escena.style.setProperty('--hc-my', cy.toFixed(4));
                if (Math.abs(tx - cx) > 0.001 || Math.abs(ty - cy) > 0.001) requestAnimationFrame(suavizar);
                else corriendo = false;
            };
        }

        /* ---------- chispas ---------- */
        var cont = document.getElementById('hcChispas');
        if (cont && !suave) {
            var n = window.innerWidth < 768 ? 8 : 16;
            for (var i = 0; i < n; i++) {
                var s = document.createElement('span');
                s.className = 'hc-chispa';
                var t = 1.5 + Math.random() * 2.5;
                s.style.width = s.style.height = t.toFixed(1) + 'px';
                s.style.left = (10 + Math.random() * 80) + '%';
                s.style.top = (15 + Math.random() * 70) + '%';
                s.style.setProperty('--hc-dx', (Math.random() * 70 - 35).toFixed(0) + 'px');
                s.style.setProperty('--hc-dy', (-50 - Math.random() * 90).toFixed(0) + 'px');
                s.style.animationDuration = (5 + Math.random() * 6).toFixed(1) + 's';
                s.style.animationDelay = (Math.random() * 6).toFixed(1) + 's';
                cont.appendChild(s);
            }
        }


        /* ---------- desplegable de controles ---------- */
        var botonAbrir = document.getElementById('hcAbrir');
        if (botonAbrir) {
            /* en pantallas chicas el hero ya es largo: los controles arrancan plegados */
            if (window.innerWidth < 1024) botonAbrir.setAttribute('aria-expanded', 'false');
            botonAbrir.addEventListener('click', function () {
                var abierto = botonAbrir.getAttribute('aria-expanded') === 'true';
                botonAbrir.setAttribute('aria-expanded', abierto ? 'false' : 'true');
            });
        }

        /* ---------- arranque ---------- */
        aplicarPaleta(PALETAS[0]);
        aplicarBpm(75);
    })();
