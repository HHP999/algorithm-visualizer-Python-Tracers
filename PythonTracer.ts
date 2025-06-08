import express from 'express';
import { Release, Tracer } from 'tracers/Tracer';
import { spawn } from 'child_process';

const pythonPath = '/usr/bin/python3'; // 根据你的环境修改 Python 解释器路径

export class PythonTracer extends Tracer {
  tagName?: string;

  constructor() {
    super('py');
  }

  async build(release: Release) {
    // 本地部署，可能不需要做什么，或加载其他资源等
    this.tagName = release.tag_name;
  }

  route(router: express.Router) {
    router.post(`/${this.lang}`, (req, res, next) => {
      const { code } = req.body;

      // 通过 child_process 调用 python 命令行程序，假设你的 Python 脚本是 tracer.py
      const pythonProcess = spawn(pythonPath, ['path/to/your/tracer.py']);

      let output = '';
      let errorOutput = '';

      pythonProcess.stdout.on('data', (data) => {
        output += data.toString();
      });

      pythonProcess.stderr.on('data', (data) => {
        errorOutput += data.toString();
      });

      pythonProcess.on('close', (codeExit) => {
        if (codeExit !== 0) {
          return next(new Error(`Python process exited with code ${codeExit}: ${errorOutput}`));
        }
        try {
          const result = JSON.parse(output);
          res.send(result);
        } catch (e) {
          next(new Error('Invalid JSON response from Python process'));
        }
      });

      // 向 python 程序传入代码（假设它从标准输入读取）
      pythonProcess.stdin.write(code);
      pythonProcess.stdin.end();
    });
  }
}
