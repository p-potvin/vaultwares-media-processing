import re

with open('vault_gui.py', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Add Task Mode Combo
task_mode_ui = '''
        # Task Mode ────────────────────────────────────────────────────────
        self.task_mode_label = self._field_label("Task Mode")
        layout.addWidget(self.task_mode_label)
        self.task_mode_combo = QComboBox()
        self.task_mode_combo.addItems(["Transcription (Parakeet)", "Video Stylization (StreamDiffusion)"])
        self.task_mode_combo.currentTextChanged.connect(self._on_task_mode_changed)
        layout.addWidget(self.task_mode_combo)
        
        layout.addWidget(self._make_separator())
        
        # Stylization Row ──────────────────────────────────────────────────
        self.stylize_widget = QWidget()
        stylize_layout = QVBoxLayout(self.stylize_widget)
        stylize_layout.setContentsMargins(0,0,0,0)
        
        self.prompt_label = self._field_label("Stylization Prompt")
        self.prompt_edit = QLineEdit()
        self.prompt_edit.setPlaceholderText("e.g. 1girl, cyberpunk, masterpiece, 4k...")
        stylize_layout.addWidget(self.prompt_label)
        stylize_layout.addWidget(self.prompt_edit)
        
        self.neg_prompt_label = self._field_label("Negative Prompt")
        self.neg_prompt_edit = QLineEdit()
        self.neg_prompt_edit.setPlaceholderText("e.g. low quality, bad anatomy...")
        stylize_layout.addWidget(self.neg_prompt_label)
        stylize_layout.addWidget(self.neg_prompt_edit)
        
        layout.addWidget(self.stylize_widget)
        self.stylize_widget.setVisible(False) # Default hidden
        
        # Transcription Container (Wrap the rest)
        self.transcription_widget = QWidget()
        transLayout = QVBoxLayout(self.transcription_widget)
        transLayout.setContentsMargins(0,0,0,0)
        
        # Core options row ────────────────────────────────────────────────
'''

content = content.replace('        # Core options row ────────────────────────────────────────────────', task_mode_ui)

# Close transcription widget layout
trans_end = '''        transLayout.addLayout(toggles_row)

        layout.addWidget(self.transcription_widget)
        
        layout.addStretch()'''

content = content.replace('''        toggles_row.addLayout(col_l)
        toggles_row.addLayout(col_r)
        layout.addLayout(toggles_row)

        layout.addStretch()''', '''        toggles_row.addLayout(col_l)
        toggles_row.addLayout(col_r)
        transLayout.addLayout(toggles_row)

        layout.addWidget(self.transcription_widget)
        
        layout.addStretch()''')

# 2. Add visibility toggle
visibility_func = '''
    def _on_task_mode_changed(self, text):
        is_stylize = "Stylization" in text
        self.stylize_widget.setVisible(is_stylize)
        self.transcription_widget.setVisible(not is_stylize)

    def start_processing(self):'''

content = content.replace('    def start_processing(self):', visibility_func)

# 3. Update processing payload
params_patch = '''        params = {
            "task_mode": self.task_mode_combo.currentText(),
            "prompt": self.prompt_edit.text(),
            "neg_prompt": self.neg_prompt_edit.text(),
            "input_file": input_path,'''

content = content.replace('''        params = {
            "input_file": input_path,''', params_patch)

# 4. Modify Thread worker
worker_patch = '''                try:
                    if "Stylization" in current_params.get("task_mode", ""):
                        output_paths = core.stylize_video(
                            input_file=current_params["input_file"], 
                            prompt=current_params.get("prompt", ""), 
                            negative_prompt=current_params.get("neg_prompt", ""),
                            progress_callback=current_params.get("progress_callback")
                        )
                    else:
                        output_paths = core.transcribe_video(**current_params)'''

content = content.replace('                try:\n                    output_paths = core.transcribe_video(**current_params)', worker_patch)

with open('vault_gui_patched.py', 'w', encoding='utf-8') as f:
    f.write(content)

print("Patch generated.")
