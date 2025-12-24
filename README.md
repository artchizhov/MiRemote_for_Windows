<html><body>
<!--StartFragment--><h1 data-start="93" data-end="141">Xiaomi Mi TV Stick Remote → Windows Controller</h1>
<p data-start="143" data-end="267">A utility for using the <strong data-start="167" data-end="208">Xiaomi Mi TV Stick Remote (MDZ‑24‑AA)</strong> on Windows as a <strong data-start="225" data-end="266">mouse, keyboard, and media controller</strong>.</p>
<p data-start="269" data-end="407">The project directly processes <strong data-start="300" data-end="334">raw HID reports over Bluetooth</strong> and allows full button remapping without additional drivers or software.</p>
<hr data-start="409" data-end="412">
<h2 data-start="414" data-end="425">Features</h2>
<ul data-start="427" data-end="1029">
<li data-start="427" data-end="514">
<p data-start="429" data-end="514">Works with <strong data-start="440" data-end="487">Xiaomi Mi Remote (Mi TV Stick / Android TV)</strong> via Bluetooth on Windows</p>
</li>
<li data-start="515" data-end="559">
<p data-start="517" data-end="559">Reads <strong data-start="523" data-end="540">raw HID input</strong> using <code data-start="547" data-end="557">pywinusb</code></p>
</li>
<li data-start="560" data-end="706">
<p data-start="562" data-end="582">Two operation modes:</p>
<ul data-start="585" data-end="706">
<li data-start="585" data-end="638">
<p data-start="587" data-end="638">🖱 <strong data-start="590" data-end="604">Mouse Mode</strong> — cursor movement, clicks, scroll</p>
</li>
<li data-start="641" data-end="706">
<p data-start="643" data-end="706">⌨ <strong data-start="645" data-end="670">Keyboard / Media Mode</strong> — keyboard keys and media actions</p>
</li>
</ul>
</li>
<li data-start="707" data-end="750">
<p data-start="709" data-end="750">Mode switching via the <strong data-start="732" data-end="741">POWER</strong> button</p>
</li>
<li data-start="751" data-end="792">
<p data-start="753" data-end="792">Button hold support with acceleration</p>
</li>
<li data-start="793" data-end="854">
<p data-start="795" data-end="821">Separate acceleration for:</p>
<ul data-start="824" data-end="854">
<li data-start="824" data-end="838">
<p data-start="826" data-end="838">mouse cursor</p>
</li>
<li data-start="841" data-end="854">
<p data-start="843" data-end="854">scrolling</p>
</li>
</ul>
</li>
<li data-start="855" data-end="986">
<p data-start="857" data-end="891">Fully configurable via JSON files:</p>
<ul data-start="894" data-end="986">
<li data-start="894" data-end="939">
<p data-start="896" data-end="939"><code data-start="896" data-end="909">config.json</code> — speed, step sizes, timing</p>
</li>
<li data-start="942" data-end="986">
<p data-start="944" data-end="986"><code data-start="944" data-end="957">device.json</code> — VID / PID and button map</p>
</li>
</ul>
</li>
<li data-start="987" data-end="1029">
<p data-start="989" data-end="1029">Ready for <strong data-start="999" data-end="1029">exe build with PyInstaller</strong></p>
</li>
</ul>
<hr data-start="1031" data-end="1034">
<h2 data-start="1036" data-end="1055">Supported Device</h2>
<ul data-start="1057" data-end="1169">
<li data-start="1057" data-end="1088">
<p data-start="1059" data-end="1088"><strong data-start="1059" data-end="1088">Xiaomi Mi TV Stick Remote</strong></p>
</li>
<li data-start="1089" data-end="1111">
<p data-start="1091" data-end="1111">Model: <strong data-start="1098" data-end="1111">MDZ‑24‑AA</strong></p>
</li>
<li data-start="1112" data-end="1127">
<p data-start="1114" data-end="1127">Bluetooth HID</p>
</li>
<li data-start="1128" data-end="1169">
<p data-start="1130" data-end="1169">VID / PID configurable in <code data-start="1156" data-end="1169">device.json</code></p>
</li>
</ul>
<hr data-start="1171" data-end="1174">
<h2 data-start="1176" data-end="1192">Control Modes</h2>
<h3 data-start="1194" data-end="1218">Mouse Mode (default)</h3>
<div class="TyagGW_tableContainer"><div tabindex="-1" class="group TyagGW_tableWrapper flex w-fit flex-col-reverse">
Button | Action
-- | --
UP / DOWN / LEFT / RIGHT | Move cursor (with acceleration)
OK | Left click
MENU | Right click
ASSIST | Middle click
NETFLIX | Scroll up
PRIME VIDEO | Scroll down

</div></div><hr data-start="1696" data-end="1699">
<h2 data-start="1701" data-end="1721">Project Structure</h2>
<pre class="overflow-visible! px-0!" data-start="1723" data-end="1823"><div class="contain-inline-size rounded-2xl corner-superellipse/1.1 relative bg-token-sidebar-surface-primary"></div></pre><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-bg-elevated-secondary text-token-text-secondary flex items-center gap-4 rounded-sm px-2 font-sans text-xs"></div></div><pre class="overflow-visible! px-0!" data-start="1723" data-end="1823"><div class="contain-inline-size rounded-2xl corner-superellipse/1.1 relative bg-token-sidebar-surface-primary"><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre! language-text"><span><span>.
├── mi_remote.py
├── mi_remote_mode_switch.py
├── config.json
├── device.json
└── README.md
</span></span></code></div></div></pre>
<hr data-start="1825" data-end="1828">
<h2 data-start="1830" data-end="1846">Configuration</h2>
<h3 data-start="1848" data-end="1865"><code data-start="1852" data-end="1865">config.json</code></h3>
<pre class="overflow-visible! px-0!" data-start="1867" data-end="2054"><div class="contain-inline-size rounded-2xl corner-superellipse/1.1 relative bg-token-sidebar-surface-primary"></div></pre><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-bg-elevated-secondary text-token-text-secondary flex items-center gap-4 rounded-sm px-2 font-sans text-xs"></div></div><pre class="overflow-visible! px-0!" data-start="1867" data-end="2054"><div class="contain-inline-size rounded-2xl corner-superellipse/1.1 relative bg-token-sidebar-surface-primary"><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre! language-json"><span><span><span class="hljs-punctuation">{</span></span><span>
  </span><span><span class="hljs-attr">"base_step_cursor"</span></span><span><span class="hljs-punctuation">:</span></span><span> </span><span><span class="hljs-number">1</span></span><span><span class="hljs-punctuation">,</span></span><span>
  </span><span><span class="hljs-attr">"max_step_cursor"</span></span><span><span class="hljs-punctuation">:</span></span><span> </span><span><span class="hljs-number">40</span></span><span><span class="hljs-punctuation">,</span></span><span>
  </span><span><span class="hljs-attr">"base_step_scroll"</span></span><span><span class="hljs-punctuation">:</span></span><span> </span><span><span class="hljs-number">1</span></span><span><span class="hljs-punctuation">,</span></span><span>
  </span><span><span class="hljs-attr">"max_step_scroll"</span></span><span><span class="hljs-punctuation">:</span></span><span> </span><span><span class="hljs-number">20</span></span><span><span class="hljs-punctuation">,</span></span><span>
  </span><span><span class="hljs-attr">"accel_time"</span></span><span><span class="hljs-punctuation">:</span></span><span> </span><span><span class="hljs-number">0.03</span></span><span><span class="hljs-punctuation">,</span></span><span>
  </span><span><span class="hljs-attr">"scroll_accel_delay"</span></span><span><span class="hljs-punctuation">:</span></span><span> </span><span><span class="hljs-number">2</span></span><span><span class="hljs-punctuation">,</span></span><span>
  </span><span><span class="hljs-attr">"scroll_delay"</span></span><span><span class="hljs-punctuation">:</span></span><span> </span><span><span class="hljs-number">0.06</span></span><span>
</span><span><span class="hljs-punctuation">}</span></span><span>
</span></span></code></div></div></pre>
<h3 data-start="2056" data-end="2073"><code data-start="2060" data-end="2073">device.json</code></h3>
<pre class="overflow-visible! px-0!" data-start="2075" data-end="2439"><div class="contain-inline-size rounded-2xl corner-superellipse/1.1 relative bg-token-sidebar-surface-primary"></div></pre><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-bg-elevated-secondary text-token-text-secondary flex items-center gap-4 rounded-sm px-2 font-sans text-xs"></div></div><pre class="overflow-visible! px-0!" data-start="2075" data-end="2439"><div class="contain-inline-size rounded-2xl corner-superellipse/1.1 relative bg-token-sidebar-surface-primary"><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre! language-json"><span><span><span class="hljs-punctuation">{</span></span><span>
  </span><span><span class="hljs-attr">"VID"</span></span><span><span class="hljs-punctuation">:</span></span><span> </span><span><span class="hljs-number">10007</span></span><span><span class="hljs-punctuation">,</span></span><span>
  </span><span><span class="hljs-attr">"PID"</span></span><span><span class="hljs-punctuation">:</span></span><span> </span><span><span class="hljs-number">12985</span></span><span><span class="hljs-punctuation">,</span></span><span>
  </span><span><span class="hljs-attr">"USAGE_BUTTONS"</span></span><span><span class="hljs-punctuation">:</span></span><span> </span><span><span class="hljs-punctuation">{</span></span><span>
    </span><span><span class="hljs-attr">"32"</span></span><span><span class="hljs-punctuation">:</span></span><span> </span><span><span class="hljs-string">"POWER"</span></span><span><span class="hljs-punctuation">,</span></span><span>
    </span><span><span class="hljs-attr">"64"</span></span><span><span class="hljs-punctuation">:</span></span><span> </span><span><span class="hljs-string">"ASSIST"</span></span><span><span class="hljs-punctuation">,</span></span><span>
    </span><span><span class="hljs-attr">"1"</span></span><span><span class="hljs-punctuation">:</span></span><span> </span><span><span class="hljs-string">"OK"</span></span><span><span class="hljs-punctuation">,</span></span><span>
    </span><span><span class="hljs-attr">"2"</span></span><span><span class="hljs-punctuation">:</span></span><span> </span><span><span class="hljs-string">"UP"</span></span><span><span class="hljs-punctuation">,</span></span><span>
    </span><span><span class="hljs-attr">"4"</span></span><span><span class="hljs-punctuation">:</span></span><span> </span><span><span class="hljs-string">"DOWN"</span></span><span><span class="hljs-punctuation">,</span></span><span>
    </span><span><span class="hljs-attr">"8"</span></span><span><span class="hljs-punctuation">:</span></span><span> </span><span><span class="hljs-string">"LEFT"</span></span><span><span class="hljs-punctuation">,</span></span><span>
    </span><span><span class="hljs-attr">"16"</span></span><span><span class="hljs-punctuation">:</span></span><span> </span><span><span class="hljs-string">"RIGHT"</span></span><span><span class="hljs-punctuation">,</span></span><span>
    </span><span><span class="hljs-attr">"512"</span></span><span><span class="hljs-punctuation">:</span></span><span> </span><span><span class="hljs-string">"MENU"</span></span><span><span class="hljs-punctuation">,</span></span><span>
    </span><span><span class="hljs-attr">"1024"</span></span><span><span class="hljs-punctuation">:</span></span><span> </span><span><span class="hljs-string">"NETFLIX"</span></span><span><span class="hljs-punctuation">,</span></span><span>
    </span><span><span class="hljs-attr">"8192"</span></span><span><span class="hljs-punctuation">:</span></span><span> </span><span><span class="hljs-string">"PRIME_VIDEO"</span></span><span><span class="hljs-punctuation">,</span></span><span>
    </span><span><span class="hljs-attr">"128"</span></span><span><span class="hljs-punctuation">:</span></span><span> </span><span><span class="hljs-string">"VOL_UP"</span></span><span><span class="hljs-punctuation">,</span></span><span>
    </span><span><span class="hljs-attr">"256"</span></span><span><span class="hljs-punctuation">:</span></span><span> </span><span><span class="hljs-string">"VOL_DOWN"</span></span><span>
  </span><span><span class="hljs-punctuation">}</span></span><span><span class="hljs-punctuation">,</span></span><span>
  </span><span><span class="hljs-attr">"MASK_BUTTONS"</span></span><span><span class="hljs-punctuation">:</span></span><span> </span><span><span class="hljs-punctuation">{</span></span><span>
    </span><span><span class="hljs-attr">"8"</span></span><span><span class="hljs-punctuation">:</span></span><span> </span><span><span class="hljs-string">"BACK"</span></span><span><span class="hljs-punctuation">,</span></span><span>
    </span><span><span class="hljs-attr">"4"</span></span><span><span class="hljs-punctuation">:</span></span><span> </span><span><span class="hljs-string">"HOME"</span></span><span>
  </span><span><span class="hljs-punctuation">}</span></span><span>
</span><span><span class="hljs-punctuation">}</span></span><span>
</span></span></code></div></div></pre>
<hr data-start="2441" data-end="2444">
<h2 data-start="2446" data-end="2461">Installation</h2>
<pre class="overflow-visible! px-0!" data-start="2463" data-end="2502"><div class="contain-inline-size rounded-2xl corner-superellipse/1.1 relative bg-token-sidebar-surface-primary"></div></pre><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-bg-elevated-secondary text-token-text-secondary flex items-center gap-4 rounded-sm px-2 font-sans text-xs"></div></div><pre class="overflow-visible! px-0!" data-start="2463" data-end="2502"><div class="contain-inline-size rounded-2xl corner-superellipse/1.1 relative bg-token-sidebar-surface-primary"><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre! language-bash"><span><span>pip install pywinusb pynput
</span></span></code></div></div></pre>
<hr data-start="2504" data-end="2507">
<h2 data-start="2509" data-end="2517">Usage</h2>
<pre class="overflow-visible! px-0!" data-start="2519" data-end="2545"><div class="contain-inline-size rounded-2xl corner-superellipse/1.1 relative bg-token-sidebar-surface-primary"></div></pre><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-bg-elevated-secondary text-token-text-secondary flex items-center gap-4 rounded-sm px-2 font-sans text-xs"></div></div><pre class="overflow-visible! px-0!" data-start="2519" data-end="2545"><div class="contain-inline-size rounded-2xl corner-superellipse/1.1 relative bg-token-sidebar-surface-primary"><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre! language-bash"><span><span>python mi_remote.py
</span></span></code></div></div></pre>
<p data-start="2547" data-end="2631">The remote must be <strong data-start="2566" data-end="2603">paired with Windows via Bluetooth</strong> before running the program.</p>
<hr data-start="2633" data-end="2636">
<h2 data-start="2638" data-end="2667">Optional: Build Executable</h2>
<pre class="overflow-visible! px-0!" data-start="2669" data-end="2722"><div class="contain-inline-size rounded-2xl corner-superellipse/1.1 relative bg-token-sidebar-surface-primary"></div></pre><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-bg-elevated-secondary text-token-text-secondary flex items-center gap-4 rounded-sm px-2 font-sans text-xs"></div></div><pre class="overflow-visible! px-0!" data-start="2669" data-end="2722"><div class="contain-inline-size rounded-2xl corner-superellipse/1.1 relative bg-token-sidebar-surface-primary"><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre! language-bash"><span><span>pyinstaller --onefile --noconsole mi_remote.py
</span></span></code></div></div></pre>
<p data-start="2724" data-end="2789">Remember to keep <code data-start="2741" data-end="2754">config.json</code> and <code data-start="2759" data-end="2772">device.json</code> next to the exe.</p>
<hr data-start="2791" data-end="2794">
<h2 data-start="2796" data-end="2810">Limitations</h2>
<ul data-start="2812" data-end="2952">
<li data-start="2812" data-end="2828">
<p data-start="2814" data-end="2828">Windows only</p>
</li>
<li data-start="2829" data-end="2856">
<p data-start="2831" data-end="2856">Works via Bluetooth HID</p>
</li>
<li data-start="2857" data-end="2916">
<p data-start="2859" data-end="2916">Does not block Windows system actions (user input only)</p>
</li>
<li data-start="2917" data-end="2952">
<p data-start="2919" data-end="2952">Requires an active user session</p>
</li>
</ul>
<hr data-start="2954" data-end="2957">
<h2 data-start="2959" data-end="2978">Why This Project</h2>
<p data-start="2980" data-end="3101">No ready-made solutions exist for using the <strong data-start="3024" data-end="3073">Xiaomi remote as an HID controller on Windows</strong>.<br data-start="3074" data-end="3077">
This project implements:</p>
<ul data-start="3103" data-end="3182">
<li data-start="3103" data-end="3125">
<p data-start="3105" data-end="3125">HID report parsing</p>
</li>
<li data-start="3126" data-end="3151">
<p data-start="3128" data-end="3151">Custom button mapping</p>
</li>
<li data-start="3152" data-end="3182">
<p data-start="3154" data-end="3182">Mouse and keyboard control</p>
</li>
</ul>
<hr data-start="3184" data-end="3187">
<h2 data-start="3189" data-end="3199">License</h2>
<p data-start="3201" data-end="3204">MIT</p><!--EndFragment-->
</body>
</html>
