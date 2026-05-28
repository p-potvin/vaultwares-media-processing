import re

with open('vault_gui.py', 'r', encoding='utf-8') as f:
    text = f.read()

new_header = '''    def _build_header(self) -> QWidget:
        w = QFrame()
        w.setObjectName("TitleBar")
        layout = QHBoxLayout(w)
        layout.setContentsMargins(16, 8, 16, 8)
        layout.setSpacing(16)

        # ── Left: Workspace Pill ──
        self.workspace_pill = QFrame()
        self.workspace_pill.setObjectName("WorkspacePill")
        pill_layout = QHBoxLayout(self.workspace_pill)
        pill_layout.setContentsMargins(8, 4, 8, 4)
        pill_layout.setSpacing(8)

        v_mark = QLabel("V")
        v_mark.setObjectName("VMark")

        ws_name_layout = QVBoxLayout()
        ws_name_layout.setSpacing(0)
        org = QLabel("VaultWares Media")
        org.setObjectName("WorkspaceOrg")
        env = QLabel("local · parakeet")
        env.setObjectName("WorkspaceEnv")
        ws_name_layout.addWidget(org)
        ws_name_layout.addWidget(env)

        chevron = QLabel("▼")
        chevron.setObjectName("WorkspaceChev")

        pill_layout.addWidget(v_mark)
        pill_layout.addLayout(ws_name_layout)
        pill_layout.addWidget(chevron)

        layout.addWidget(self.workspace_pill)

        # ── Center: Spacer ──
        layout.addStretch()

        # ── Right: Search, Language, Theme, Avatar ──
        self.search_btn = QPushButton("🔍 Search or jump to...   ⌘K")
        self.search_btn.setObjectName("SearchBtn")
        layout.addWidget(self.search_btn)

        divider = QFrame()
        divider.setFrameShape(QFrame.Shape.VLine)
        divider.setObjectName("HeaderDivider")
        layout.addWidget(divider)

        # Language switch
        self.lang_combo = QComboBox()
        self.lang_combo.setFixedWidth(60)
        self.lang_combo.addItems(["EN", "QC"])
        self.lang_combo.currentTextChanged.connect(self.change_language)

        # Theme selector
        self.theme_combo = QComboBox()
        self.theme_combo.setFixedWidth(200)
        for t in self.themes:
            self.theme_combo.addItem(t.name)

        is_dark = True
        try:
            from PySide6.QtGui import QPalette
            import PySide6.QtWidgets
            app_inst = PySide6.QtWidgets.QApplication.instance()
            if app_inst:
                win_color = app_inst.palette().color(QPalette.ColorRole.Window).value()
                if win_color > 128:
                    is_dark = False
        except Exception:
            pass

        default_theme_name = "Golden Slate" if is_dark else "Codex Solar Light"
        for i, t in enumerate(self.themes):
            if t.name == default_theme_name:
                self.theme_combo.setCurrentIndex(i)
                self.current_theme = t
                break

        self.theme_combo.currentTextChanged.connect(self.change_theme)

        layout.addWidget(self.lang_combo)
        layout.addWidget(self.theme_combo)

        # Avatar
        self.avatar = QLabel("AD")
        self.avatar.setObjectName("Avatar")
        self.avatar.setFixedSize(28, 28)
        self.avatar.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.avatar)

        return w'''

text = re.sub(r'    def _build_header\(self\).*?return w', new_header, text, flags=re.DOTALL)
text = re.sub(r'\s*self\.title_label\.setText\([^)]*\)', '', text)
text = re.sub(r'\s*self\.theme_label\.setText\([^)]*\)', '', text)
text = re.sub(r'self\.status_icon\.setStyleSheet\(.*?\)', r'self.status_icon.setStyleSheet(f"color: {t.accent}; font-weight: bold;")', text)

with open('vault_gui.py', 'w', encoding='utf-8') as f:
    f.write(text)
